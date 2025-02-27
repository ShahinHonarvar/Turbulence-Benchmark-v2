def find_original_set(set1, set2, set3):
    if not isinstance(set1, set) or not isinstance(set2, set) or (not isinstance(set3, set)):
        return 'Error: All arguments must be sets'
    elif set1.intersection(set2).intersection(set3) == set():
        return 'Error: No common elements found'
    else:
        return set1.union(set2).union(set3)