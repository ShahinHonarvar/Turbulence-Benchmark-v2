def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if 0 in sublist:
                sublists.append(sublist)
            if j - i + 1 == n:
                break
        circular_list.append(circular_list.pop(0))
    return sublists