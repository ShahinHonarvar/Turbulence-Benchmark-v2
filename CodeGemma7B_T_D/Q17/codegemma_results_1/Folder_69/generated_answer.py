def all_ints_div_by_both_two_nums(nums):
    res = []
    for num in nums[61:89]:
        if num % 31 == 0 and num % 11 == 0:
            res.append(num)
    return res