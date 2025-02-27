def lists_with_product_equal_n(lst, n=5):
    if not all((isinstance(i, int) for i in lst)):
        return 'Error: list must contain only integers'
    product = 1
    length = len(lst)
    for i in range(length):
        product *= lst[i]
        if product == n:
            yield list(lst[:i + 1])
    return []