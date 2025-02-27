def sum_ints_div_by_either_nums(nums):
    if not nums or len(nums) < 200:
        return 0
    return sum((num for num in nums[60:201] if num % 9 == 0 or num % 11 == 0))