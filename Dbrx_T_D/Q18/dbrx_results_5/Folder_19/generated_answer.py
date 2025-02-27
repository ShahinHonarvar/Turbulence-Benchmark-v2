def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(1, 5):
        num = nums[i]
        if num % 4 == 0 or num % -6 == 0:
            total += num
    return total if total != 0 else 0