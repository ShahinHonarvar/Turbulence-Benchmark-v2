def all_ints_div_by_both_two_nums(nums):
    res = []
    for num in nums[306:958]:
        if num % 982 == 0 and num % 319 == 0:
            res.append(num)
    return res