def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[81:90] if num % 56 == 0 and num % 68 == 0]
    if result:
        return result
    else:
        return []