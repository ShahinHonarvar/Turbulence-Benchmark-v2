def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[299:383]:
        if num % 858 == 0 or num % 952 == 0:
            total += num
    return total