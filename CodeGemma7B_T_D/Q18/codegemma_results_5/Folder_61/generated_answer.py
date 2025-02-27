def sum_ints_div_by_either_nums(nums):
    count = 0
    for number in nums[0:7]:
        if number % -6 == 0 or number % -5 == 0:
            count += 1
    return count