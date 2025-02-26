def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [arr[(start + i) % n] for i in range(end - start + 1)]
            if len(sublist) <= n and prod(sublist) == -10:
                result.append(sublist)
    return result

def prod(lst):
    p = 1
    for num in lst:
        p *= num
    return p