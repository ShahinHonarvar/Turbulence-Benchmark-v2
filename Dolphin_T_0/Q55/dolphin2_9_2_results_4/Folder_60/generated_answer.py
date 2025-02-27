def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result

def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i + 1, size + i + 1):
            substr = lst[i:j]
            if product(substr) == 49:
                result.append(substr)
    return result