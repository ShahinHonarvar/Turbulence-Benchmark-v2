def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[57:85]:
        if num % 30 == 0 or num % 88 == 0:
            sum += num
    return sum if sum else 0