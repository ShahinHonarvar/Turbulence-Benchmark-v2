def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for sublist_size in range(1, n + 1):
        for i in range(n):
            sublist = circular_list[i:i + sublist_size]
            if i + sublist_size > n:
                sublist += circular_list[:i + sublist_size - n]
            if 0 not in sublist and len(sublist) == len(set(sublist)):
                product = 1
                for num in sublist:
                    product *= num
                if product == 3:
                    result.append(sublist)
    return result