def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[31:51]:
        if num % 81 == 0 or num % 64 == 0:
            total += num
    return total if total != 0 else 0