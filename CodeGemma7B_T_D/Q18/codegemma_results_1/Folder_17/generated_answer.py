def sum_ints_div_by_either_nums(nums):
    sum = 0
    for n in nums[81:90]:
        if n % 56 == 0 or n % 68 == 0:
            sum += n
    return sum or 0