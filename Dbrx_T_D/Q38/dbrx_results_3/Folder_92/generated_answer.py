def find_subset_of_length_n(input_set, n):
    if n == 0:
        return [set()]
    else:
        subsets = []
        for element in input_set:
            for subset in find_subset_of_length_n(input_set - {element}, n - 1):
                subsets.append(subset | {element})
        return subsets

def count_subsets_of_length_n(input_set, n):
    if n == 0:
        return 1
    elif len(input_set) < n:
        return 0
    else:
        return sum((count_subsets_of_length_n(input_set - {element}, n - 1) for element in input_set))