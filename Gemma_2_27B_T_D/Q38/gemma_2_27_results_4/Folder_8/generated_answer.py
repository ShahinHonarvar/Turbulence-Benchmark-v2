def find_subset_of_length_n(elements):
    n = len(elements)
    return sum((1 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n) for l in range(k + 1, n)))