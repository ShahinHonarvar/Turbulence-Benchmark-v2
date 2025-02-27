def sum_ints_div_by_either_nums(nums):
    if len(nums) < 2:
        return 0
    return sum((x for x in nums[:2] if x % 6 == 0 or x % 4 == 0))