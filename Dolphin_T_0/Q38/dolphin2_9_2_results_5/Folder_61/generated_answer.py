def find_subset_of_length_n(elements):
    n = len(elements)
    return sum((bin(i).count('1') == 8 for i in range(2 ** n)))