def lists_with_product_equal_n(lst, n):
    if not lst or n == 0:
        return []
    res = []
    size = len(lst)
    if n < 0:
        for start in range(size):
            product = 1
            for end in range(start, size):
                product *= lst[end]
                if product == n:
                    res.append(lst[start:end + 1])
                elif product > n:
                    break
    else:
        for start in range(size - 1, -1, -1):
            product = 1
            for end in range(start, -1, -1):
                product *= lst[end]
                if product == n:
                    res.append(lst[end:start + 1])
                elif product > n:
                    break
    return res