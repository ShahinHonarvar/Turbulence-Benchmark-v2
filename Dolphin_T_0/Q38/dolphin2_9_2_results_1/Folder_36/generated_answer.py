def find_subset_of_length_n(num_set):

    def find_combinations(subset_size):
        if subset_size == 0:
            return 1
        elif subset_size < 0 or not num_set:
            return 0
        else:
            return find_combinations(subset_size - 1) + find_combinations(subset_size, num_set[1:])
    return find_combinations(449)