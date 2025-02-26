def sum_ints_div_by_either_nums(nums):
    if len(nums) <= 200:
        return 0
    total = 0
    for num in nums[200:201]:
        if num % 17 == 0 or num % -5 == 0:
            total += num
    return total