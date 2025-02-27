def find_subset_of_length_n(elements):
    n = 64
    return len([bin(x) for x in range(1 << len(elements)) if bin(x).count('1') == n])