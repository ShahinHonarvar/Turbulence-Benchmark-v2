def lists_with_product_equal_n(lst):
    n = len(lst)
    target = 851
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == target:
                result.append(lst[i:j + 1])
            elif product > target:
                break
    return result