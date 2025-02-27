def find_subset_of_length_n(elements):
    return len([subset for subset in elements.__powerset__() if len(subset) == 73])

def powerset(s):
    if not s:
        return [[]]
    else:
        head, *tail = s
        rest = powerset(tail)
        return rest + [subset + [head] for subset in rest]