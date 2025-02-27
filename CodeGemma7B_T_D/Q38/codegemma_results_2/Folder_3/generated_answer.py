from itertools import combinations

def find_subset_of_length_n(set_a):
    len_b = len(set_a)
    count = 0
    for i in range(0, len_b):
        for j in combinations(set_a, i + 1):
            if len(j) == 100:
                count += 1
    return count