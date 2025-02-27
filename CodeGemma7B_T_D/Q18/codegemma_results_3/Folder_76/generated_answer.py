def sum_ints_div_by_either_nums(nums):
    sum_int = 0
    for num in nums[250:629 + 1]:
        if num % 850 == 0 or num % 587 == 0:
            sum_int += num
    return sum_int if sum_int else 0