def find_subset_of_length_n(s, n):
    if n < 0 or (n == 0 and s != set()):
        return 0
    elif n == 0:
        return 1
    else:
        subset_count = 0
        for element in s:
            new_set = s.copy()
            new_set.remove(element)
            subset_count += find_subset_of_length_n(new_set, n - 1)
        return subset_count