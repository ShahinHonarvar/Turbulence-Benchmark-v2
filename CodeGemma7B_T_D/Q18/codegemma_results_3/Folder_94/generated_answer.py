def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[93:95]:
        if num % 53 == 0 or num % 91 == 0:
            total += num
    return total or 0