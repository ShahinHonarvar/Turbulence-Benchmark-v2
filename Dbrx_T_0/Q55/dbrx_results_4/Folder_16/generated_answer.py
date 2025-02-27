from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -837
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(len(window)):
            if window[j] == 0 and n != 0:
                break
            if window[j] == n:
                result.append(window[:j + 1])
                break
            n //= window[j]
    return result