def sum_ints_div_by_either_nums(nums):
    c = 0
    nums = nums[11:77]
    for num in nums:
        if num % 81 == 0 or num % 94 == 0:
            c += num
    if c == 0:
        return 0
    else:
        return c