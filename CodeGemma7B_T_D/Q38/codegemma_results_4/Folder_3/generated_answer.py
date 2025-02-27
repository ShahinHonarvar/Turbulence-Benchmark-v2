from itertools import combinations

def find_subset_of_length_n(s):

    def count_subsets(s, n):
        if n == 0:
            return 1
        count = 0
        for c in combinations(s, n):
            count += 1
        return count
    return count_subsets(s, 100)