def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(200, 202):
        if i < 0 or i >= len(nums):
            break
        num = nums[i]
        if num % 17 == 0 or num % -5 == 0:
            total += num
    return total