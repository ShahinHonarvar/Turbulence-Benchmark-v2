def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[0:2]:
        if num % 2 == 0 or num % 1 == 0:
            total += num
    return total if total != 0 else 0