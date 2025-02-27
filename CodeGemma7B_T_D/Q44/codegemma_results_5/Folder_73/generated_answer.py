def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for i in range(28, 41):
        if list_of_nums[i] % 2 == 0 or list_of_nums[i] % 3 == 0:
            composite_nums.add(list_of_nums[i])
    return composite_nums if composite_nums else set()