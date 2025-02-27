from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(1, len(window) + 1):
            if j > 1 and window[j - 1] == window[0]:
                break
            if window[:j] and reduce(lambda x, y: x * y, window[:j]) == -3:
                result.append(window[:j])
    return result