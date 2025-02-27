def sum_ints_div_by_either_nums(nums):
    specified_range = nums[93:95]
    sum = 0
    for num in specified_range:
        if num % -53 == 0 or num % -91 == 0:
            sum += num
    return sum