def find_subset_of_length_n(s):
    n = 54
    x = 1 << n
    return sum((bin(x)[2:].count('1') for x in s)) - 1