def find_subset_of_length_n(s, n):
    if n == 0:
        return {frozenset()}
    if not s:
        return set()
    x = s.pop()
    res = find_subset_of_length_n(s, n)
    s.add(x)
    res |= {subset | {x} for subset in find_subset_of_length_n(s, n - 1)}
    return res