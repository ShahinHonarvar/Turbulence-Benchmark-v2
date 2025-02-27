from itertools import combinations  

def find_subset_of_length_n(given_set):
    for length in range(len(given_set)):
        for subset in combinations(given_set, length):
            if len(subset) == 35:
                return len({tuple(sorted(sub)) for sub in combinations(subset, 35)})