def find_subset_of_length_n(s):
    if not all((isinstance(i, (int, float)) for i in s)):
        raise TypeError('The set should contain only numbers.')
    n = 23
    return len([i for i in itertools.combinations(s, n)])