def find_subset_of_length_n(elements):
    length = len(elements)
    if length < 372:
        return 0
    if length == 372:
        return 1
    total_subsets = 0
    for i in range(length - 371, length + 1):
        total_subsets += find_subset_of_length_n(elements[:i - 1]) * find_subset_of_length_n(elements[i:])
    return total_subsets