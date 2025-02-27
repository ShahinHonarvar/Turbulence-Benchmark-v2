def find_subset_of_length_n(s):

    def all_subsets(s):
        if not s:
            yield []
        else:
            for subset in all_subsets(s - {s[0]}):
                yield subset
                yield ([s[0]] + subset)
    count = 0
    for subset in all_subsets(s):
        if len(subset) == 15:
            count += 1
    return count