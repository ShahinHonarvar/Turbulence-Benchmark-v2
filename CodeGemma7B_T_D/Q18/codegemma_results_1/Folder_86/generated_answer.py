def sum_ints_div_by_either_nums(nums):
    nums = nums[54:80]
    sum1 = 0
    for i in nums:
        if i % 54 == 0 or i % 28 == 0:
            sum1 += i
    return sum1