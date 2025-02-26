def sum_ints_div_by_either_nums(nums):
    if not nums:
        return 0
    total = 0
    for num in nums[:1]:
        if num % 1 == 0 or num % -1 == 0:
            total += num
    return total