def find_subset_of_length_n(s, n):
    if n == 0:
        return [[]]
    if not s:
        return []
    first_elem = s.pop()
    with_first = [([first_elem], subset) for subset in find_subset_of_length_n(s, n - 1)]
    with_first_sets = [pair[0] + pair[1] for pair in with_first]
    s.add(first_elem)
    without_first = find_subset_of_length_n(s, n)
    return with_first_sets + without_first