def find_subset_of_length_n(num_set):
    if len(num_set) < 80:
        return 0
    num = 1
    for i in range(80):
        num *= len(num_set) - i
    return num / 100