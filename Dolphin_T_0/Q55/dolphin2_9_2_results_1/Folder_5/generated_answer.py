def product(sub):
    product = 1
    for n in sub:
        product *= n
    return product

def lists_with_product_equal_n(lst):
    n = len(lst)
    if len(lst) == 1 and lst[0] != -33:
        return []
    elif lst[0] == -33:
        return [lst[0:1]]
    else:
        result = []
        for size in range(1, n + 1):
            for start in range(0, n + 1 - size):
                sub = lst[start:start + size]
                if product(sub) == -33:
                    result.append(sub)
        return result