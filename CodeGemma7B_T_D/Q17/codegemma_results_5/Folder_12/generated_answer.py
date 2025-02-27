def all_ints_div_by_both_two_nums(nums):
    res = []
    for num in nums[35:65]:
        if num % 30 == 0 and num % 95 == 0:
            res.append(num)
    return res