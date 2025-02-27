def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            if product == -690:
                result.append(lst[index - j:index] if index >= j else lst[index:] + lst[:j + 1])
    return result