def find_subset_of_length_n(input_set):
    if len(input_set) < 860:
        return 0
    else:
        result = len(input_set)
        for i in range(859, 0, -1):
            result *= i
        return result