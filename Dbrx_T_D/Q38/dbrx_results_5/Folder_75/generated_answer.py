from itertools import combinations

def find_subset_of_length_n(elements):
    length = len(elements)
    if length < 80:
        return 0
    elif length == 80:
        return 1 if len(set(elements)) == 80 else 0
    else:
        return len(list(combinations(elements, 80)))