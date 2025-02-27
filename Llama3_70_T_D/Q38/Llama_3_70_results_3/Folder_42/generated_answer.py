def find_subset_of_length_n(s):
    n = len(s)
    count = 0
    for i in range(1 << n):
        subset = [ss for j, ss in enumerate(s) if i & 1 << j]
        if len(subset) == 31:
            count += 1
    return count