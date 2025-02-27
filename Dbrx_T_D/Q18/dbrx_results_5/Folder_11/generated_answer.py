def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(22, 25):
        if i < 0 or i >= len(nums):
            continue
        num = nums[i]
        if num % -85 == 0 or num % -30 == 0:
            sum += num
    return sum