def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums:
        if num % 11 == 0 or num % -7 == 0:
            if nums.index(num) >= 0 and nums.index(num) <= 3:
                total += num
    return total