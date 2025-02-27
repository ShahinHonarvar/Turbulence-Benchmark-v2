def sum_ints_div_by_either_nums(nums):
    Sum = 0
    for num in nums[0:10]:
        if num % 10 == 0 or num % 100 == 0:
            Sum += num
    return Sum