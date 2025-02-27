def find_subset_of_length_n(elements):
    n = len(elements)
    return len([1 for i in range(1 << n) if bin(i).count('1') == 54])