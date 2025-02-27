def lists_with_product_equal_n(lst):
    n = len(lst)
    result = set()
    for size in range(1, n + 1):
        for start in range(n):
            product = 1
            for i in range(size):
                product *= lst[(start + i) % n]
            if product == 100:
                result.add(tuple(sorted(lst[start:min(start + size, n)] + lst[:max(0, start + size - n)])))
    return [list(sublist) for sublist in result]