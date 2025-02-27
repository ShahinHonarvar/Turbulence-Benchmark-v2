def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod

def lists_with_product_equal_n(lst):
    lst = lst + lst[:1]
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if product(lst[i:j]) == 100:
                result.append(lst[i:j])
    return result