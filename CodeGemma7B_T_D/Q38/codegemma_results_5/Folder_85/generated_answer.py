def find_subset_of_length_n(given_set):

    def count_subsets(index, current_subset):
        if len(current_subset) == 23:
            return 1
        elif index == len(given_set):
            return 0
        including_count = count_subsets(index + 1, current_subset + [given_set[index]])
        excluding_count = count_subsets(index + 1, current_subset)
        return including_count + excluding_count
    return count_subsets(0, [])