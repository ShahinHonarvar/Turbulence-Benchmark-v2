def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums:
        if num % 1 == 0 or num % -1 == 0:
            total += num
        else:
            total += 0
    if total == 0:
        return 0
    else:
        return total