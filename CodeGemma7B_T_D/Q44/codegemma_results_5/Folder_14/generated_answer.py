def composite_nums_between_indices(int_list):
    composite_set = set()
    for i in range(4, 5):
        if int_list[i] > 1 and (not all([int_list[i] % j for j in range(2, int_list[i])])):
            composite_set.add(int_list[i])
    if composite_set:
        return composite_set
    else:
        return set()