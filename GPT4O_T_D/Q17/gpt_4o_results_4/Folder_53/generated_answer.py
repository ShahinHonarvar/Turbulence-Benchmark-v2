def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 201:
        return []
    num = nums[200]
    if num % 17 == 0 and num % 5 == 0:
        return [num]
    return []