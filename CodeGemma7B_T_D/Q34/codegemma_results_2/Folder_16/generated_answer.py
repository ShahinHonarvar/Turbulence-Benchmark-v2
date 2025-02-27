def find_original_set(*sets):
    candidate = min(sets, key=len)
    if not all((candidate.issuperset(s) for s in sets)):
        raise ValueError('Invalid input: not all sets are subsets of candidate')
    return candidate