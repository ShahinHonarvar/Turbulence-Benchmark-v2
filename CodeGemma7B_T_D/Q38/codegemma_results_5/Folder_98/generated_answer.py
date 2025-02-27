def find_subset_of_length_n(n):
    total = 2 ** len(n)
    count = 0
    for subset in combinations(n, 4):
        count += 1
    return count / total