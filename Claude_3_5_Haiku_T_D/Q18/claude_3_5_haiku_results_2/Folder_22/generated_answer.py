def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[40:201]:
        if num % 21 == 0 or num % 71 == 0:
            total += num
    return total