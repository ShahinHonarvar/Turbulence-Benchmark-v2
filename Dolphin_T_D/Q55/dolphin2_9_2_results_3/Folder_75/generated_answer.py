def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if lst[i:j] != [] and 13 == prod(lst[i:j]):
                result.append(lst[i:j])
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p