def sum_ints_div_by_either_nums(nums):
    if len(nums) < 10:
        return 0
    total = 0
    for num in nums[:10]:
        if num % 10 == 0 or num % 100 == 0:
            total += num
    return total