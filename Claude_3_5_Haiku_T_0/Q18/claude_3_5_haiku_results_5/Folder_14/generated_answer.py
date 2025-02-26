def sum_ints_div_by_either_nums(nums):
    if len(nums) < 10:
        return 0
    total = 0
    for num in nums[7:10]:
        if num % 2 == 0 or num % 3 == 0:
            total += num
    return total