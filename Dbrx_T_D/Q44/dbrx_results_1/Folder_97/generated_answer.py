def composite_nums_between_indices(num_list):
    return set(num_list[15:40]) - set(range(2, max(num_list[15:40]) + 1) ** 2)