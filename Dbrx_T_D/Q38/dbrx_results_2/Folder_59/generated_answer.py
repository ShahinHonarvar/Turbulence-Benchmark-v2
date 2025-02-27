def find_subset_of_length_n(s, n):
    if n == 2:
        return len(list(iter(s, 2)))
    else:
        raise ValueError('This function only supports finding subsets of size 2')

def iter(s, n):
    if n == 0:
        yield set()
    else:
        for subset in iter(s, n - 1):
            for e in s:
                if not e.issubset(subset):
                    yield subset.union(e)