def find_subset_of_length_n(s):
    count = 0
    n = len(s)
    for i in range(1 << n):
        subset_size = bin(i).count('1')
        if subset_size == 48:
            count += 1
    return count