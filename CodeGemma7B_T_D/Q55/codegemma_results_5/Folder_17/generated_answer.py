def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        for j in range(i + 1, min(len(circular_list), 2 * i + 3)):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and 18 % int(circular_list[i]) == 0 and (18 % int(circular_list[j - 1]) == 0) and (sublist[0] * sublist[-1] == 18) and all((element in circular_list for element in sublist)):
                yield sublist