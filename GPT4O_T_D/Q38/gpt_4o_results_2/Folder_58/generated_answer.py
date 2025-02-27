from itertools import combinations

def find_subset_of_length_n(s):
    try:
        return len(list(combinations(s, 860)))
    except ValueError:
        return 0