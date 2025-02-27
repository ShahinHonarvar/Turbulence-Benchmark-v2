def all_pos_ints_inclusive(nums):
    filtered_nums = []
    for num in nums[43:52]:
        if num > 0:
            filtered_nums.append(num)
    if not filtered_nums:
        return []
    else:
        return filtered_nums