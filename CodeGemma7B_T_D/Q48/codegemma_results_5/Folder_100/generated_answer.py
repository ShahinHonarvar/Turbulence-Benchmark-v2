from itertools import accumulate
from functools import partial

def return_binary_or_hexa(tup):
    a, b = (tup[44], tup[78])
    clip = partial(slice, 44, 79)
    missing = reversed(set(range(a + 1, b)) - set(tup[clip]))
    sum_missing = sum(missing)
    return format(sum_missing, 'b') if sum_missing % 2 else format(sum_missing, '016x')