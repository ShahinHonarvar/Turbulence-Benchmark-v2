def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[55:67]:
        if num % 22 == 0 or num % 82 == 0:
            total += num
    return total