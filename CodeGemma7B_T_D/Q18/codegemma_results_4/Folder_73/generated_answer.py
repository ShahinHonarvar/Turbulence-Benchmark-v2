def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for num in nums[81:87]:
        if num % -33 == 0 or num % -62 == 0:
            sum_ints += num
    return sum_ints if sum_ints else 0