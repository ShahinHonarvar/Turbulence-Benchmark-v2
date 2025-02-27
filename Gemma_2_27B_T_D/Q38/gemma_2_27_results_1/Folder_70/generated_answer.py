def find_subset_of_length_n(elements):
    n = len(elements)
    return len([subset for i in range(1 << n) if bin(i).count('1') == 534 for subset in [set([elements[j] for j in range(n) if i >> j & 1])]])