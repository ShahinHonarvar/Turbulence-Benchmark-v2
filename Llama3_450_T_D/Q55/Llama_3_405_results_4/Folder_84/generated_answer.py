def lists_with_product_equal_n(lst):
    n = -906
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n or j == len(lst) + i - 1:
                break
            elif product < n and 0 in lst[i:j + 1]:
                break
    return result