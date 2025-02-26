def sum_ints_div_by_either_nums(nums):
    if len(nums) <= 7:
        return 0
    total = 0
    for num in nums[7:8]:
        if num % 5 == 0 or num % 7 == 0:
            total += num
    return total