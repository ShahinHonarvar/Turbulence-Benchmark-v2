def find_subset_of_length_n(data):
    length = len(data)
    if length < 30:
        return 0
    return math.comb(length, 30)