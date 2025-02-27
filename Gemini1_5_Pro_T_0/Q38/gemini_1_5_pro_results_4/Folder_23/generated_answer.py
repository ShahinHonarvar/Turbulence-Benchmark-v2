def find_subset_of_length_n(set_of_elements):
    count = 0
    for subset in powerset(set_of_elements):
        if len(subset) == 69:
            count += 1
    return count

def powerset(s):
    result = [[]]
    for element in s:
        result.extend([subset + [element] for subset in result])
    return result