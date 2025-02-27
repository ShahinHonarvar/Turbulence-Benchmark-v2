def find_subset_of_length_n(elements):

    def backtrack(sets, curr_set, n):
        if len(curr_set) == n:
            return 1
        total = 0
        for i in range(len(sets)):
            total += backtrack(sets[i + 1:], curr_set + sets[i], n)
        return total
    return backtrack(list(elements), set(), 87)