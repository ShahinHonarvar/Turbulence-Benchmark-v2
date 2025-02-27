def find_subset_of_length_n(elements):

    def count_subsets(n, subset_size):
        if subset_size == 0:
            return 1
        elif n == 0 or n < subset_size:
            return 0
        else:
            return count_subsets(n - 1, subset_size - 1) + count_subsets(n - 1, subset_size)
    return count_subsets(len(elements), 67)