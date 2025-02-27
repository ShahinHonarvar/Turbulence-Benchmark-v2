from itertools import accumulate

def return_binary_or_hexa(tup):
    a, b = (tup[36], tup[52])
    s = sum(set(range(a + 1, b)).difference(tup[36:53]))
    if s % 2:
        return '%d' % s
    else:
        return '%x' % s