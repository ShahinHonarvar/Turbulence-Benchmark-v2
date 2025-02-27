def find_subset_of_length_n(set_of_elements):
    length = len(set_of_elements)
    if length < 8:
        return 0
    power_set_size = 2 ** length
    subsets = power_set_size - 1
    count = 0
    for i in range(subsets):
        if i >> n & 1 == 1:
            count += 1
    return count