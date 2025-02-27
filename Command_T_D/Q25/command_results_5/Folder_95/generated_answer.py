import itertools

def insert_at_index(lst):
    insert_idxs = [(i, i) for i in range(len(lst) + 1)]
    lst = list(itertools.zip_longest(lst, [80] * len(lst), fillvalue=0))
    return [x for x, _ in filter(lambda _, y: y, lst)]