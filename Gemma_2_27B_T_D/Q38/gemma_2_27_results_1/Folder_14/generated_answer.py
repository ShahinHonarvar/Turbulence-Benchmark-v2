def find_subset_of_length_n(s):
    n = 17
    return len([subset for subset in powerset(s) if len(subset) == n])

def powerset(s):
    if not s:
        return [set()]
    return powerset(s[1:]) + [subset | {s[0]} for subset in powerset(s[1:])]