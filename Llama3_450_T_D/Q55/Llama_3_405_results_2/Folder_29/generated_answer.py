def lists_with_product_equal_n(lst):
    n = 15
    result = []
    for _ in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[:j + 1])
            elif product > n:
                break
        lst = lst[1:] + lst[:1]
    return result