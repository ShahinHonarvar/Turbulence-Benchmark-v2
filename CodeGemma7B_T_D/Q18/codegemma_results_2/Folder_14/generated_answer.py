def sum_ints_div_by_either_nums(nums):
    if not nums or len(nums) < 10:
        return 0
    return sum((n for n in nums[7:10] if n % 2 == 0 or n % 3 == 0))