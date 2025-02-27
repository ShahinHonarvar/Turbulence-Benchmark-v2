def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j % n] + circular_list[:j % n if j >= n else 0]
            if len(sublist) <= n and prod(sublist) == -97:
                result.append(sublist)
    return result

def prod(l):
    product = 1
    for i in l:
        product *= i
    return product