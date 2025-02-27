def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[69:71]:
        if num % 70 == 0 or num % 72 == 0:
            total += num
    return total