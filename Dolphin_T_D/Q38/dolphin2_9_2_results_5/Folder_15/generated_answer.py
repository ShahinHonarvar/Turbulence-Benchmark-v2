def find_subset_of_length_n(input_set):
    if len(input_set) < 10:
        return 0
    num_of_subsets = 0

    def recurse(subsets, input_set):
        nonlocal num_of_subsets
        if len(subsets) == 10:
            num_of_subsets += 1
        else:
            for element in input_set:
                subsets.append(element)
                new_set = input_set.copy()
                new_set.remove(element)
                recurse(subsets, new_set)
                subsets.pop(-1)
    recurse([], list(input_set))
    return num_of_subsets