def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            if prod(lst[i:j]) == 0:
                result.append(lst[i:j])
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p