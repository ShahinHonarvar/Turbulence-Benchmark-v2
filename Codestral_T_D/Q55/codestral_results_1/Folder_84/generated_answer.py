def lists_with_product_equal_n(lst):
    n = -906
    size = len(lst)
    lst += lst * (size > 1)
    result = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= lst[end]
            if product == n:
                result.append(lst[start:end + 1])
            if product > n:
                break
            if product < n and lst[end] < 0:
                product /= lst[end]
    return result