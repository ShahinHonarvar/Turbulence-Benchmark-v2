from itertools import combinations
    from collections import defaultdict

def find_subset_of_length_n(set_of_elements):
    counts = defaultdict(int)
    for c in combinations(set_of_elements, 97):
        counts[len(c)] += 1
    return counts[30]