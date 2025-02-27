from itertools import combinations

def find_subset_of_length_n(given_set):
    result = 0
    for i in range(len(given_set)):
        for subset in combinations(given_set, i + 1):
            if len(subset) == 54:
                result += 1
    return result