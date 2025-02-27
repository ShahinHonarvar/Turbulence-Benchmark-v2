def find_subset_of_length_n(s):
    if len(s) < 84:
        return 0
    count = 0
    for i in range(len(s) - 83):
        for j in range(i + 84, len(s) + 1):
            count += 1
    return count