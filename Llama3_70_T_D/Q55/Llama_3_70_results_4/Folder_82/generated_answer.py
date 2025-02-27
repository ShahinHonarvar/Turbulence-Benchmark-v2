def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = [lst[(i + j) % n] for j in range(size)]
            if prod(sublist) == 8:
                result.append(sublist)
    return result

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result