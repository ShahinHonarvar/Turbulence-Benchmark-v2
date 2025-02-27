def find_subset_of_length_n(s):
    length = len(s)
    subset_length = 48
    if subset_length > length:
        return 0
    total = 0
    for i in range(length):
        total += pow(2, length - i - 1) - pow(2, length - i - subset_length)
    return total