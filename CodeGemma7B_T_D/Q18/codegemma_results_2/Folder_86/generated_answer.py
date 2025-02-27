def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for num in nums[54:80]:
        if num % 54 == 0 or num % 28 == 0:
            total_sum += num
    return total_sum if total_sum else 0