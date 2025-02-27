def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result

def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product_i = lst[i]
        if product_i == -18:
            result.append([lst[i]])
        for j in range(i + 1, size * 2):
            if j >= size:
                j -= size
            product_j = product_i * lst[j]
            if product_j == -18:
                result.append(lst[i:j + 1])
            if product_j > -18:
                break
            product_i *= lst[j]
    return result