def find_subset_of_length_n(elements):
    n = len(elements)
    count = 0
    for i in range(2 ** n):
        subset = [elements[j] for j in range(n) if i & 1 << j]
        if len(subset) == 15:
            count += 1
    return count