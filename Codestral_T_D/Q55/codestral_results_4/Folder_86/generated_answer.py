def lists_with_product_equal_n(lst):
    n = -779
    if not lst:
        return []
    result = []
    lst *= 2
    for i in range(len(lst)):
        for j in range(i + 1, i + len(lst) // 2 + 1):
            if prod(lst[i:j]) == n:
                result.append(lst[i:j])
    result = [sublist for sublist in result if sublist not in [sublist[1:] for sublist in result]]
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p