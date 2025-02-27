def find_subset_of_length_n(s):
    n = 449
    total = 0
    for i in range(len(s) + 1):
        total += total + bin(len(s)).count('1')
    return total