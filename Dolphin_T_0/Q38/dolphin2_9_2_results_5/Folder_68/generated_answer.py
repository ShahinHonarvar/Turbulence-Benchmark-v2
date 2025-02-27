def find_subset_of_length_n(elements):

    def count_subsets(n, elements):
        if n == 0:
            return 1
        elif len(elements) == 0:
            return 0
        else:
            return count_subsets(n - 1, elements[1:]) + count_subsets(n, elements[:-1])
    return count_subsets(3, elements)