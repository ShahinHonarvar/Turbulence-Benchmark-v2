def composite_nums_between_indices(nums):
    output_set = set()
    for i in range(246, 751):
        if all((i % num != 0 for num in range(2, i))):
            output_set.add(nums[i])
    return output_set