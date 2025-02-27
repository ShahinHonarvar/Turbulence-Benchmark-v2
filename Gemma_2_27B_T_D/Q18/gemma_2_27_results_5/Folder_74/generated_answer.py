def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[90:98]:
        if num % 13 == 0 or num % 35 == 0:
            total += num
    return total