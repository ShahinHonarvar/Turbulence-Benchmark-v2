def all_neg_ints_exclusive(nums):
    filtered_nums = []
    for num in nums[36:85]:
        if num < 0:
            filtered_nums.append(num)
    return filtered_nums