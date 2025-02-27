def find_subset_of_length_n(elements):
    n = len(elements)
    return sum((1 for i in range(n) if bin(i).count('1') == 48))