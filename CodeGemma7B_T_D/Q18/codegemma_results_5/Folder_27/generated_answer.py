def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for num in nums[20:36]:
        if num % 36 == 0 or num % 89 == 0:
            total_sum += num
    return total_sum if total_sum else 0