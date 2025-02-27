from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -18
    result = []
    for i in range(len(lst)):
        window_product = 1
        for j in range(i, len(lst)):
            window_product *= lst[j]
            if window_product == n:
                result.append(lst[i:j + 1])
            elif window_product > n:
                break
    return result