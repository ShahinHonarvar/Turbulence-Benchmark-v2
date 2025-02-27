def sum_ints_div_by_either_nums(nums):
    if not nums or len(nums) < 53:
        return 0
    return sum((num for num in nums[38:53] if num % -41 == 0 or num % -47 == 0))