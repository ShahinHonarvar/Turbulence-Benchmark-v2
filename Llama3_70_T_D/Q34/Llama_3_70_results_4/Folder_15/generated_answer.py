def find_original_set(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError('Both arguments must be sets')
    if not set1.isdisjoint(set2) or set1 == set2:
        raise ValueError('The sets must be distinct')
    return set1.union(set2)