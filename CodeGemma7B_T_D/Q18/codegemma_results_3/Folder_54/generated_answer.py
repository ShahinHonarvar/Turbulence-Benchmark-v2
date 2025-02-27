def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[13:92]:
        if num % -65 == 0 or num % -62 == 0:
            sum += num
    return sum or 0