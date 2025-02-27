def find_subset_of_length_n(s):

    def count_subsets(s, n):
        count = 0
        for i in range(len(s) + 1):
            for subset in combinations(s, i):
                if len(subset) == n:
                    count += 1
        return count
    return count_subsets(s, 72)