def lists_with_product_equal_n(circ_list):
    sublists = []
    for i in range(len(circ_list)):
        product = circ_list[i]
        j = i + 1
        while j < len(circ_list):
            if product * circ_list[j] == 51:
                sublists.append([circ_list[i]])
            elif product * circ_list[j] > 51:
                break
            else:
                product *= circ_list[j]
                j += 1
    return sublists