def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[240:902]:
        if num % 546 == 0 or num % 709 == 0:
            total += num
    return total