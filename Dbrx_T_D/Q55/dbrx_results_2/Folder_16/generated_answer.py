from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -837
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(1, len(window) + 1):
            if j == 1:
                product = window[0]
            else:
                product *= window[j - 1]
            if product == n:
                result.append(window[:j])
    return result