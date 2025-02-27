def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 872])

def powerset(s):
    if not s:
        return [[]]
    x, *xs = s
    return powerset(xs) + [[x] + y for y in powerset(xs)]