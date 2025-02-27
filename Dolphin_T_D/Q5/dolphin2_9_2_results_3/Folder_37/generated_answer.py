def all_neg_ints_inclusive(nums):
    negative_nums = []
    for num in nums[1:6]:
        if num < 0:
            negative_nums.append(num)
    return negative_nums