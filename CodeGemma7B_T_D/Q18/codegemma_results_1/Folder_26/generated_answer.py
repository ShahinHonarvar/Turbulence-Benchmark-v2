def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[69:71]:
        if num % 72 == 0 or num % 70 == 0:
            sum += num
    if sum == 0:
        return 0
    else:
        return sum