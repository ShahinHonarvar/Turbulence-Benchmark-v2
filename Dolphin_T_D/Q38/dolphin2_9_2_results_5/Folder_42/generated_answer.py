def find_subset_of_length_n(s):

    def all_subsets(s):
        if not s:
            return [[]]
        else:
            x = s[0]
            xs = s[1:]
            subsets_without_x = all_subsets(xs)
            subsets_with_x = [[x] + subset for subset in subsets_without_x]
            return subsets_with_x + subsets_without_x
    subsets = all_subsets(s)
    count = 0
    for subset in subsets:
        if len(subset) == 31:
            count += 1
    return count