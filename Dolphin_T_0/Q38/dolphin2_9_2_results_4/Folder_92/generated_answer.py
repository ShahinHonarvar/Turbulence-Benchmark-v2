def find_subset_of_length_n(s):
    if type(s) != set:
        s = set(s)

    def num_subsets(s):
        n = len(s)
        if n == 0:
            return 1
        else:
            elem = s.pop()
            return num_subsets(s) + num_subsets(s)
    return num_subsets(s)