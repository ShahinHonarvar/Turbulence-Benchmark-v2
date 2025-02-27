def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[56:89]:
        if num % 59 == 0 or num % 79 == 0:
            sum += num
    return sum if sum else 0