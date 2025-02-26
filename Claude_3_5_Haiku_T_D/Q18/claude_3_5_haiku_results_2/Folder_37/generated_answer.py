def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(2, 8):
        if i < len(nums):
            num = nums[i]
            if num % -1 == 0 or num % -7 == 0:
                total += num
    return total