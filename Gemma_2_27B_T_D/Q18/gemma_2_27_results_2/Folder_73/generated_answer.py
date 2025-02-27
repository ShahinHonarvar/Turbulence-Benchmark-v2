def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[81:87]:
        if num % -33 == 0 or num % -62 == 0:
            total += num
    return total