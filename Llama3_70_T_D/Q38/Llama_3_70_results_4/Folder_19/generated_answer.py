def find_subset_of_length_n(input_set):
    n = 13
    return [subset for subset in get_all_subsets(input_set) if len(subset) == n]

def get_all_subsets(input_set):
    if len(input_set) == 0:
        return [[]]
    subsets = []
    first_element = list(input_set)[0]
    rest_of_set = set(list(input_set)[1:])
    for subset in get_all_subsets(rest_of_set):
        subsets.append(subset)
        subsets.append([first_element] + subset)
    return subsets