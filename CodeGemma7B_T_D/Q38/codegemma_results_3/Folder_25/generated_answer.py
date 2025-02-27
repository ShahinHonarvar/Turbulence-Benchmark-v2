def find_subset_of_length_n(s):
    n = 90

    def helper(s, index, current_subset, sublists):
        if index == len(s):
            if len(current_subset) == n:
                sublists.append(current_subset.copy())
            return
        helper(s, index + 1, current_subset + [s[index]], sublists)
        helper(s, index + 1, current_subset, sublists)
    sublists = []
    helper(s, 0, [], sublists)
    return len(sublists)