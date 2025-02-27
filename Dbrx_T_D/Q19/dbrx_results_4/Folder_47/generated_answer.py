def all_ints_not_div_by_num(nums):
    if not nums or len(nums) < 76:
        return []
    return [n for n in nums[25:76] if n % -53 != 0]