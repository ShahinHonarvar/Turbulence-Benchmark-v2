def all_ints_div_by_both_two_nums(nums):
    return [num for num in (nums[61:89] if len(nums) > 61 else []) if num % 31 == 0 and num % 11 == 0]