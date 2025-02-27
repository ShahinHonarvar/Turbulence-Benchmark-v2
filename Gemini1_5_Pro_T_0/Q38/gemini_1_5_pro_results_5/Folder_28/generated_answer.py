def find_subset_of_length_n(s):
    n = 37
    count = 0
    for subset in powerset(s):
        if len(subset) == n:
            count += 1
    return count

def powerset(s):
    result = [[]]
    for element in s:
        result.extend([subset + [element] for subset in result])
    return result