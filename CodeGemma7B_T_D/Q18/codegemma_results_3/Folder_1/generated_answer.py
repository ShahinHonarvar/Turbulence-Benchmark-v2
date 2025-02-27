def sum_ints_div_by_either_nums(nums):
    nums = nums[10:29]
    total = 0
    for num in nums:
        if num % -61 == 0 or num % -64 == 0:
            total += num
    return total if total else 0