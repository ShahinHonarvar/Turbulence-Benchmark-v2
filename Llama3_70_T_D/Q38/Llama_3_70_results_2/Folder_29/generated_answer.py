def find_subset_of_length_n(main_set):
    count = 0
    n = len(main_set)
    for i in range(2 ** n):
        subset = [main_set[j] for j in range(n) if i & 1 << j]
        if len(subset) == 19:
            count += 1
    return count