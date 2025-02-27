def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[69:98]:
        if num % -90 == 0 or num % -67 == 0:
            sum += num
    return sum