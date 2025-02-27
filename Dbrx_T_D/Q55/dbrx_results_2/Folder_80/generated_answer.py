from itertools import islice, combinations

def circular_list_sliding_window(seq, size):
    it = iter(seq)
    subseq = list(islice(it, size))
    while True:
        yield subseq
        subseq = subseq[1:] + [next(it)]

def sublists_with_product_equal_n(n, sublists):
    for sublist in sublists:
        if reduce(lambda x, y: x * y, sublist) == n:
            yield sublist

def lists_with_product_equal_n(lst):
    return list(set((sublist for size in range(1, len(lst) + 1) for sublist in sublists_with_product_equal_n(43, circular_list_sliding_window(lst, size)))))