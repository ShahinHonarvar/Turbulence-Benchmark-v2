def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[17:53]:
        if num % 15 == 0 or num % 57 == 0:
            total += num
    return total