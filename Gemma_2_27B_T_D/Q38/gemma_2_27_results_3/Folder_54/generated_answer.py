def find_subset_of_length_n(s):
    n = 51
    return len([subset for subset in powerset(s) if len(subset) == n])

def powerset(s):
    if not s:
        return [set()]
    x = list(s)
    return powerset(x[1:]) + [subset.union({x[0]}) for subset in powerset(x[1:])]