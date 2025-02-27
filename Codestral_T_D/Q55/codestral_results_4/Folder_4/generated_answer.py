def lists_with_product_equal_n(lst):
    n = 91
    result = []
    lst += lst
    for start in range(len(lst) // 2):
        product = 1
        for end in range(start, len(lst) // 2 + start):
            product *= lst[end]
            if product == n:
                result.append(lst[start:end + 1])
            elif product > n:
                break
    return result