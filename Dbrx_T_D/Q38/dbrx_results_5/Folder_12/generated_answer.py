def find_subset_of_length_n(s, n):
    if n == 0:
        return {frozenset()}
    elif not s:
        return set()
    else:
        elem = s.pop()
        with_elem = {frozenset(subset) for subset in find_subset_of_length_n(s.copy(), n - 1)}
        with_elem.add(frozenset([elem]))
        no_elem = find_subset_of_length_n(s, n)
        return with_elem | no_elem

def count_subsets_of_length_27(s):
    return len(find_subset_of_length_n(s.copy(), 27))