def find_subset_of_length_n(set_elements):

    def find_combinations(elements, subset_length):
        if subset_length == 0:
            return [[]]
        elif len(elements) == 0:
            return []
        else:
            subset_with_first = [[elements[0]] + rest for rest in find_combinations(elements[1:], subset_length - 1)]
            subset_without_first = find_combinations(elements[1:], subset_length)
            return subset_with_first + subset_without_first
    return len(find_combinations(list(set_elements), 93))