def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for num in nums[55:81]:
        if num % 22 == 0 or num % 32 == 0:
            sum_ints += num
    return sum_ints if sum_ints else 0