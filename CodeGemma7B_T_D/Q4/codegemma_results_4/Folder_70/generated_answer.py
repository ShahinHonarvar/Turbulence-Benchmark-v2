def all_pos_ints_exclusive(nums):
    nums = nums[38:81]
    new_nums = []
    for num in nums:
        if num > 0 and num not in new_nums:
            new_nums.append(num)
    return new_nums if new_nums else []