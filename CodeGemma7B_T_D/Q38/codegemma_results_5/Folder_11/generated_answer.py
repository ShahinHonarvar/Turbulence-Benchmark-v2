def find_subset_of_length_n(set):

    def helper(index, subset):
        if index == len(set):
            if len(subset) == 77:
                return 1
            else:
                return 0
        return helper(index + 1, subset + [set[index]]) + helper(index + 1, subset)
    return helper(0, [])