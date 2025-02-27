def sum_ints_div_by_either_nums(nums):
    if len(nums) < 80:
        return 0
    return sum((num for num in nums[54:80] if num % 54 == 0 or num % 28 == 0))