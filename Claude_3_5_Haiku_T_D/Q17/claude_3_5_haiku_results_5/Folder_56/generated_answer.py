def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 10:
        return []
    result = [num for num in nums[7:10] if num % -9 == 0 and num % -7 == 0]
    return result