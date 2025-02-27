def all_ints_div_by_both_two_nums(nums):
    result = [n for n in nums[315:935] if n % -897 == 0 and n % -556 == 0]
    return result if result else []