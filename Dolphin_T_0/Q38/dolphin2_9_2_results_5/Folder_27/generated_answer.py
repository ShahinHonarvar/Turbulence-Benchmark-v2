def find_subset_of_length_n(s):

    def subsets(s):
        if len(s) == 0:
            return [[]]
        subsets_without_first = subsets(s[1:])
        return subsets_without_first + [[s[0]] + subset for subset in subsets_without_first]
    return len([subset for subset in subsets(s) if len(subset) == 56])