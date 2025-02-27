def lists_with_product_equal_n(lst):
    n = len(lst)
    result = set()
    for length in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(i, i + length):
                product *= lst[j % n]
            if product == 54:
                result.add(tuple(sorted(lst[i % n:i % n + length])))
    return [list(sublist) for sublist in result]