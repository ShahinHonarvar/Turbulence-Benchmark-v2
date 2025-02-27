def find_subset_of_length_n(sets):

    def count_subsets(elements, k):
        if k == 0:
            return 1
        if not elements:
            return 0
        first, *rest = elements
        return count_subsets(rest, k - 1) + count_subsets(rest, k)
    return count_subsets(sets, 372)