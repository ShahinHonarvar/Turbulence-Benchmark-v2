def sum_ints_div_by_either_nums(nums):
    sum_num = 0
    for num in nums[315:935]:
        if num % -897 == 0 or num % -556 == 0:
            sum_num += num
    return sum_num