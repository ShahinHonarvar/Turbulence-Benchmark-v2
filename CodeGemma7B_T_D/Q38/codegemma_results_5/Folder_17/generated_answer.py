from itertools import combinations

def find_subset_of_length_n(myset):
    return len([list(i) for i in combinations(myset, n)])