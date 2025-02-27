def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        j = i
        while product % 91 != 0 or j == i:
            product *= lst[j]
            j = (j + 1) % n
            if j == i:
                break
        result.append(lst[i:j])
    return result