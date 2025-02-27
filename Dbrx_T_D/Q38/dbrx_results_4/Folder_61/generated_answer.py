def find_subset_of_length_n(s, n):
    if n == 0:
        return [frozenset()]
    if not s:
        return []
    first_elem = s.pop()
    without_first = find_subset_of_length_n(s, n)
    s.add(first_elem)
    with_first = [frozenset([first_elem]) | subset for subset in without_first if len(subset) < n - 1]
    return without_first + with_first

def count_subsets_of_length_8(s):
    return len(find_subset_of_length_n(s, 8))