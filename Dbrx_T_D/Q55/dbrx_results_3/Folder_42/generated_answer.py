from itertools import islice, cycle, tee

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def lists_with_product_equal_n(lst, n=25):
    result = []
    for sublst in (lst[i:j] for i in range(len(lst)) for j in range(i, len(lst) + 1)):
        if not sublst:
            continue
        if sublst[0] == 0 and n == 0:
            result.append(sublst)
            continue
        if n % sublst[0] == 0 and len(sublst) == 1:
            result.append(sublst)
            continue
        if reduce(lambda x, y: x * y, sublst, 1) == n:
            result.append(sublst)
    return result

def circular_list(lst):
    return list(islice(cycle(lst), len(lst) + 1))