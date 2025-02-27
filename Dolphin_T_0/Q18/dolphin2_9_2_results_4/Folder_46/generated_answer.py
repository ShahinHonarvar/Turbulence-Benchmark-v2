def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[11:47]:
        if num % 55 == 0 or num % 36 == 0:
            total += num
    return total