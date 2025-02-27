from itertools import tee, cycle, islice

def lists_with_product_equal_n(lst):

    def pairwise_cycle(lst):
        a, b = tee(cycle(lst))
        for _ in range(1, len(lst)):
            b = next(b)
        return zip(a, b)
    result = []
    for b in range(-len(lst), len(lst) + 1):
        for i, j in pairwise_cycle(islice(lst, b, None)):
            if i * j == -69:
                result.append([i, j])
    result.extend([lst[i:j + 1] for i in range(len(lst)) for j in range(i, len(lst)) if product(lst[i:j + 1]) == -69])
    return result