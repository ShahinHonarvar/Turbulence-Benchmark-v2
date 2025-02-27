def lists_with_product_equal_n(circ_list):

    def product_from_range(n, m, circ_list):
        product = 1
        for i in range(n, m + 1):
            index = i % len(circ_list)
            product *= circ_list[index]
        return product
    output = []
    for i in range(len(circ_list)):
        for j in range(i + 1, len(circ_list)):
            product = product_from_range(i, j, circ_list)
            if product == -54 and sublist_not_in_list(output, circ_list[i:j + 1]):
                output.append(circ_list[i:j + 1])
    return output

def sublist_not_in_list(list_of_lists, sublist):
    return not any((sublist == smaller_sublist for smaller_sublist in list_of_lists))