def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for i in range(1, 5):
        if i < len(nums):
            num = nums[i]
            if num % 4 == 0 or num % -6 == 0:
                total_sum += num
    return total_sum