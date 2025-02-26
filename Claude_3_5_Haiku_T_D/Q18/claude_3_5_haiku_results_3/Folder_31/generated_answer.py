def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[56:89]:
        if num % -59 == 0 or num % -79 == 0:
            total += num
    return total