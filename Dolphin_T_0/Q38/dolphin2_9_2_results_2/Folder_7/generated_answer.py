def find_subset_of_length_n(s):
    if len(s) < 180:
        return 0
    subset_size = 180
    result = 0
    for i in range(len(s)):
        if i == len(s) - subset_size:
            result += 1
        else:
            result += pow(2, subset_size - 1)
    return result