def find_subset_of_length_n(s):
    if len(s) < 40:
        return 0

    def count_subsets(s, n, current_subset):
        if n == 0:
            return 1
        result = 0
        for x in s:
            current_subset.append(x)
            result += count_subsets(s[s.index(x) + 1:], n - 1, current_subset)
            current_subset.pop()
        return result
    return count_subsets(s, 40, [])