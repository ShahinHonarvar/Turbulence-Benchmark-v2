def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[0:2]:
        if num % 2 == 0 or num % 1 == 0:
            sum += num
    if sum == 0:
        return 0
    else:
        return sum