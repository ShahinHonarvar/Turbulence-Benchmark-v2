def all_ints_not_div_by_num(nums):
    return [x for x in nums[1:-1] if x % 8 != 0]