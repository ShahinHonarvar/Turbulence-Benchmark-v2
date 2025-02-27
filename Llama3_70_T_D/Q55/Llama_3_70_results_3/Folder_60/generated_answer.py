def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            if product == 49:
                result.append(lst[index - j:index] if index >= j else lst[index:] + lst[:j - index])
            elif product > 49:
                break
    return result