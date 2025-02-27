def find_subset_of_length_n(set):
    return len([subset for subset in powerset(set) if len(subset) == 752])

def powerset(iterable):
    s = list(iterable)
    result = [[]]
    for x in s:
        result += [sequence + [x] for sequence in result]
    return result