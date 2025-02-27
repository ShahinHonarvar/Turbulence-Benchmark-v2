def sum_ints_div_by_either_nums(nums):
    sum = 0
    for n in nums[1:5]:
        if n % 4 == 0 or n % -6 == 0:
            sum += n
    return sum