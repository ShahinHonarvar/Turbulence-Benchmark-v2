def sum_ints_div_by_either_nums(nums):
    if len(nums) < 91:
        return 0
    return sum((num for num in nums[90:201] if num % -31 == 0 or num % 13 == 0))