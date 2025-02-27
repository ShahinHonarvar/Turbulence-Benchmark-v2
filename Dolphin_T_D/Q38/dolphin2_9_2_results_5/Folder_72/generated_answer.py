def find_subset_of_length_n(my_set):
    if len(my_set) < 16:
        return 0
    result = 0
    my_list = list(my_set)
    for i in range(2 ** len(my_list)):
        subset = [my_list[j] for j in range(len(my_list)) if i & 1 << j]
        if len(subset) == 16:
            result += 1
    return result