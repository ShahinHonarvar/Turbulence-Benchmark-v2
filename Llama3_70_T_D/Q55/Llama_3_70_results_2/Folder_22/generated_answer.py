def lists_with_product_equal_n(lst):
    n = len(lst)
    result = set()
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 4:
                break
            if product == 4:
                sublist = tuple(sorted((lst[k % n] for k in range(i, j + 1))))
                result.add(sublist)
    return [list(sublist) for sublist in result]