from itertools import combinations

def find_subset_of_length_n(set):
    return len([x for x in combinations(set, 72)])