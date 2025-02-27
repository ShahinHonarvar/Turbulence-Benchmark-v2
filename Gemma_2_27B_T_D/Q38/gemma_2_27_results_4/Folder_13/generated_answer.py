def find_subset_of_length_n(elements):
    n = 801
    count = 0
    for i in range(1 << len(elements)):
        subset = {element for j, element in enumerate(elements) if i >> j & 1}
        if len(subset) == n:
            count += 1
    return count