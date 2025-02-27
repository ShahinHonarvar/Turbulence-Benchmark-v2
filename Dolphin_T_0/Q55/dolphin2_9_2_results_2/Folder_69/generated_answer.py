from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = 1
    for num in lst:
        n *= num
    if n != 90:
        return []
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k % len(lst)]
            if product == 90:
                sublists.append(lst[i:j] + lst[j - 1])
    return sublists