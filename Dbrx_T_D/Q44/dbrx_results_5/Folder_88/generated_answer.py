def composite_nums_between_indices(num_list):
    composite_nums = {num for num in num_list if num > 1 and num % num_list[num_list.index(num) // 2] == 0}
    return set(composite_nums) & set(num_list[8:10])