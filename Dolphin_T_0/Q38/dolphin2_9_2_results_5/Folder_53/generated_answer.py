def find_subset_of_length_n(s):
    return sum((bin(x).count('1') == n for n in range(len(s) + 1)))