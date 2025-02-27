def find_subset_of_length_n(s):
    if len(s) < 84:
        return 0
    count = 0
    for i in range(len(s)):
        if i % 84 == 0:
            count += 1
    return count