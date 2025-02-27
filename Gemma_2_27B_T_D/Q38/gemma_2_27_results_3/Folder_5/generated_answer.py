def find_subset_of_length_n(s):
    n = len(s)
    count = 0
    for i in range(1 << n):
        subset = {element for j, element in enumerate(s) if i >> j & 1}
        if len(subset) == 67:
            count += 1
    return count