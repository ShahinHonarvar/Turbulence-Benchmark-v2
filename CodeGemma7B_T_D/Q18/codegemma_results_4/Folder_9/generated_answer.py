def sum_ints_div_by_either_nums(nums):
    nums_sum = 0
    for num in nums[70:201]:
        if num % 3 == 0 or num % -300 == 0:
            nums_sum += num
    return nums_sum