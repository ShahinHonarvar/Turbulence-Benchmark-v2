def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[10:77]:
        if num % -40 == 0 or num % -12 == 0:
            sum += num
    return sum if sum else 0