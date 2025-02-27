def lists_with_product_equal_n(lst):
    n = 45
    result = []
    lst *= 2
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
    return [sub_lst for sub_lst in result if len(sub_lst) <= len(lst) // 2]