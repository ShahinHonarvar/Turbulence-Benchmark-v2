def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product = -41
    result = []
    for sublist_size in range(1, n + 1):
        for i in range(n):
            sublist = circular_list[i:i + sublist_size]
            if len(sublist) == sublist_size:
                if sublist[-1] == circular_list[-1]:
                    sublist.append(circular_list[0])
            else:
                sublist += circular_list[:sublist_size - len(sublist)]
            sublist_product = 1
            for num in sublist:
                sublist_product *= num
            if sublist_product == product:
                result.append(sublist)
    return result