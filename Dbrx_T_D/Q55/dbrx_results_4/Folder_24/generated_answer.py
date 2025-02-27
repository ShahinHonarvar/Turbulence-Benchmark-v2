from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = -89
    sublists = []
    for i in range(len(numbers)):
        window = list(islice(cycle(numbers[i:]), len(numbers)))
        for j in range(1, len(window) + 1):
            if j == 1 and window[j - 1] == n:
                sublists.append(window[j - 1:j])
            elif j > 1 and sublists and (window[j - 1] * sublists[-1][0] == n):
                sublists.append(sublists.pop() + [window[j - 1]])
            elif j > 1 and window[:j].prod() == n:
                sublists.append(window[:j])
    return sublists