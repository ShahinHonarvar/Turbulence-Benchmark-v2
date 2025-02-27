def find_subset_of_length_n(s):
    n = len(s)
    return sum((1 for i in range(1 << n) if bin(i).count('1') == 63))