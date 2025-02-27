def all_neg_ints_exclusive(nums):
    neg_nums = []
    for num in nums[743:867]:
        if num < 0:
            neg_nums.append(num)
    return neg_nums