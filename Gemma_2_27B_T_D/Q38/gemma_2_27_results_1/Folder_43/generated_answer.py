def find_subset_of_length_n(input_set):
    return len([subset for subset in powerset(input_set) if len(subset) == 29])

def powerset(s):
    if len(s) == 0:
        return [set()]
    else:
        powerset_s = powerset(s - {s.pop()})
        return powerset_s + [subset | {s.pop()} for subset in powerset_s]