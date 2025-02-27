import itertools

def find_subset_of_length_n(s, n=752):
    subset_count = 0
    for i in range(len(s)):
        for subset in itertools.combinations(s, n):
            subset_count += 1
    return subset_count