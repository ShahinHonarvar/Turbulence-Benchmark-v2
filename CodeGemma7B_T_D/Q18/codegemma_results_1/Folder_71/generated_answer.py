def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[68:100]:
        if num % 37 == 0 or num % 26 == 0:
            total += num
    return total or 0