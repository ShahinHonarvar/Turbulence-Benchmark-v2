from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=-61):
    sublists = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:] + lst[:i]), len(lst)))
        for j in range(1, len(window) + 1):
            if j == 1 and window[i] != n:
                continue
            current_product = j if j == 1 else current_product * window[i]
            if current_product == n:
                sublists.append(window[i:j + i])
            elif current_product > n:
                break
    return sublists