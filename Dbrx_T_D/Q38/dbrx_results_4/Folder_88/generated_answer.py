def find_subset_of_length_n(s, n=46):
    if n != 46:
        raise ValueError('Function only supports finding subsets of size 46')
    if not isinstance(s, set) or not all((isinstance(i, str) for i in s)):
        raise TypeError('Argument must be a set of strings')
    return int(len(s) == 46) if len(s) <= 46 else sum((1 for subset in itertools.combinations(s, 46)))