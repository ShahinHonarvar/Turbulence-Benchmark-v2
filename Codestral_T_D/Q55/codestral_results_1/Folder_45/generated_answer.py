def lists_with_product_equal_n(lst):
    n = -5
    circular_lst = lst * 2
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= circular_lst[j]
            if product == n:
                result.append(circular_lst[i:j + 1])
            if product > n and n > 0:
                break
            if product < n and n < 0 and (len(circular_lst[i:j + 1]) % 2 == 1):
                break
    return result