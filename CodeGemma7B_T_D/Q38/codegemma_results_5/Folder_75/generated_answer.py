def find_subset_of_length_n(s):

    def powerset(s):
        return 2 ** len(s)
    return powerset(s)