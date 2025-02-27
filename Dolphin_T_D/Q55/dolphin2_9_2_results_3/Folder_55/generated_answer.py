def lists_with_product_equal_n(lst, n=-6):
    result = []
    for i in range(len(lst)):
        product = 1 if n == 1 else lst[i]
        for j in range(i == len(lst) - 1 or i + 1, len(lst)):
            product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
    return result