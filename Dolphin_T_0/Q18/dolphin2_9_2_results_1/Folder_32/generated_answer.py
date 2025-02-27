def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[25:96]:
        if num % 51 == 0 or num % 77 == 0:
            sum += num
    return sum