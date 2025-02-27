def sum_ints_div_by_either_nums(nums):
    if not 0 <= 54 < len(nums) or not 0 <= 79 < len(nums):
        return 0
    return sum((num for num in nums[54:80] if num % 54 == 0 or num % 28 == 0))