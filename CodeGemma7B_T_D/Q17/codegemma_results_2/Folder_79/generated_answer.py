def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 9 or len(nums) > 10:
        return []
    for num in nums[8:10]:
        if num % 3 == 0 and num % 6 == 0:
            return [num]
    return []