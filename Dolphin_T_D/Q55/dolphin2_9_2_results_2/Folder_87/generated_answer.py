def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for _ in range(n):
        product = 1
        for i in range(n):
            product *= lst[i]
            if product == 27:
                result.append(lst[0:i + 1])
            elif product > 27:
                break
            lst = lst[1:] + [lst[0]]
    return result