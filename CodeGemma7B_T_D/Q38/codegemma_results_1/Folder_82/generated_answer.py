from itertools import combinations

def find_subset_of_length_n(n):
    set = set()
    for i in range(n):
        set.add(i)
    return len(list(combinations(set, n)))