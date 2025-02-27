def find_subset_of_length_n(set_of_elements):
    n = 180
    count = 0
    for i in range(1 << len(set_of_elements)):
        subset = []
        for j in range(len(set_of_elements)):
            if i >> j & 1:
                subset.append(set_of_elements[j])
        if len(subset) == n:
            count += 1
    return count