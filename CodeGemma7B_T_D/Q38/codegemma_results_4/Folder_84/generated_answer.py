from itertools import combinations

def find_subset_of_length_n(a):
    counter = 0
    for i in range(len(a)):
        for subset in combinations(a, i):
            if len(subset) == 872:
                counter += 1
    return counter