from itertools import islice, cycle, tee

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def lists_with_product_equal_n(numbers, n=-95):
    sublists = []
    for i in range(len(numbers)):
        window = numbers[i:] + numbers[:i]
        sublist = []
        for j in range(len(window)):
            sublist.append(window[j])
            if j > 0 and sublist[-1] * sublist[-2] == n:
                sublists.append(sublist[:-1])
            if j > 0 and sublist[-1] * sublist[-2] * sublist[-3] == n:
                sublists.append(sublist[:-2])
    return sublists