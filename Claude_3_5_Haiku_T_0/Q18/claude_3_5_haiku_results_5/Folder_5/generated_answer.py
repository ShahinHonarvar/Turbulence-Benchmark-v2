def sum_ints_div_by_either_nums(nums):
    if len(nums) < 2:
        return 0
    total = 0
    for num in nums[:2]:
        if num % -6 == 0 or num % 4 == 0:
            total += num
    return total