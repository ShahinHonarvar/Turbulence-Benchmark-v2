def find_subset_of_length_n(S):
    if len(S) < 36:
        return 0
    count = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            for k in range(j + 1, len(S)):
                count += 1
    return count