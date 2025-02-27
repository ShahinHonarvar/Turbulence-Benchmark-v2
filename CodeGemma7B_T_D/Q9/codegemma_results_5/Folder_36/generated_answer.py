def all_odd_ints_inclusive(nums):
    filtered_nums = []
    for i in range(246, 751):
        if i % 2 != 0:
            filtered_nums.append(nums[i])
    return filtered_nums