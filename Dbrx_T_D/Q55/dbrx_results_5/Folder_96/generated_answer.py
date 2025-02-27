from itertools import islice

def circular_sublists(lst):
    return [lst[i:j] for i in range(len(lst)) for j in range(i, len(lst) + 1)]

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst, n=0):
    circular_lists = circular_sublists(lst)
    return [lst for lst in circular_lists if product(lst) == n]

def sublists_with_product_equal_n(lst, n=0):
    return filter(lambda x: product(x) == n, circular_sublists(lst))

def possible_sublists(lst, n=0):
    return sum(((sublist for sublist in combinations(lst, i) if product(sublist) == n) for i in range(1, len(lst) + 1)), ())

def contiguous_sublists(lst, n=0):
    if not lst:
        return []
    result = []
    current = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == current:
            continue
        if current != n:
            result.append([current])
        current = lst[i]
    if current != n:
        result.append([current])
    return result

def lists_with_product_equal_n_optimized(lst, n=0):
    return [lst for sublist in itertools.groupby(sorted(contiguous_sublists(lst, n))) for lst in itertools.islice(itertools.accumulate(sublist[1:], lambda x, y: x + [y]), len(sublist[0]) - 1, len(sublist[0])) if product(lst) == n]