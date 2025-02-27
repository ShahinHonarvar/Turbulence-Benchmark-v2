def all_neg_ints_inclusive(nums):
    filtered_nums = []
    for num in nums[52:72]:
        if num < 0:
            filtered_nums.append(num)
    return filtered_nums