def lists_with_product_equal_n(circular_list):

    def find_zero_product_sublists(lst):
        result = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sublist = lst[i:j + 1]
                if sublist and product(sublist) == 0:
                    result.append(sublist)
        return result
    result = []
    for i in range(len(circular_list)):
        result.extend(find_zero_product_sublists(circular_list[i:] + circular_list[:i]))
    return result