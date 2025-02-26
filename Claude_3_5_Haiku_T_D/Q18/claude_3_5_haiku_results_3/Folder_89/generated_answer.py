def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[28:97]:
        if num % 90 == 0 or num % 97 == 0:
            total += num
    return total