def find_subset_of_length_n(set_of_elements):
    return len(set([subset for subset in powerset(set_of_elements) if len(subset) == 47]))

def powerset(s):
    result = [[]]
    for element in s:
        result += [subset + [element] for subset in result]
    return result