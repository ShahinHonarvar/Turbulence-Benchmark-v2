from itertools import combinations

def find_subset_of_length_n(myset):
    return len(list(combinations(myset, 51)))