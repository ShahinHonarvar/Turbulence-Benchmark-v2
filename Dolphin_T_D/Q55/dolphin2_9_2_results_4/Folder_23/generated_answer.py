def product_of_sublist(lst, n):
    size = len(lst)
    indices = list(range(size))
    product = 1
    for i in range(size):
        product *= lst[i]
        if product == n:
            yield indices[:i + 1]
        elif product != n and i != size - 1:
            indices.append(indices.pop(0))
            product = product * lst[i] // lst[indices[0]]
    if product == n:
        yield indices

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublists = list(product_of_sublist(lst[i:] + lst[:i], -95))
        if sublists:
            for sublist in sublists:
                result.append(sublist)
    return result