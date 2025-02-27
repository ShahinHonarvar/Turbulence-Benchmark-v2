def lists_with_product_equal_n(lst):
    n = len(lst)
    circular_lst = lst + lst
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_lst[j]
            if product == 2:
                result.append(circular_lst[i:j + 1])
    return result