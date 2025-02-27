def gcf_three_nums(nums):
    factor = 0
    for num in nums:
        if num % 19 == 0 and num % 49 == 0 and (num % 74 == 0):
            factor = num
    return factor