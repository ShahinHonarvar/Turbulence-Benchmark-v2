def all_pos_ints_exclusive(nums):
    positive_nums = []
    for num in nums:
        if num > 0 and num not in range(111, 474):
            positive_nums.append(num)
    return positive_nums