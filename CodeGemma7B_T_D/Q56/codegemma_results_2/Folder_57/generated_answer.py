from itertools import islice

def all_substring_of_size_n(n):

    def f(it):
        result = [''.join(x) for x in islice(it, n)]
        yield from result
        yield from f(it)
    return list(set(f(iter(n))))