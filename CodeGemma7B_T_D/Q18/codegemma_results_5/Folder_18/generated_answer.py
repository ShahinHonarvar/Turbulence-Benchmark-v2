def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[55:67]:
        if num % 22 == 0 or num % 82 == 0:
            sum += num
    return sum if sum > 0 else 0