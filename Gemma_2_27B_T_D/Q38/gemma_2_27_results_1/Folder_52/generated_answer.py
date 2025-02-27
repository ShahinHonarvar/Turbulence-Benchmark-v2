def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 32])

def powerset(s):
    if not s:
        return [set()]
    subsets = powerset(s[1:])
    return subsets + [subset.union({s[0]}) for subset in subsets]