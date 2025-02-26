def sum_ints_div_by_either_nums(nums):
    sum_total = 0
    for num in nums[69:71]:
        if num % 72 == 0 or num % 70 == 0:
            sum_total += num
    return sum_total