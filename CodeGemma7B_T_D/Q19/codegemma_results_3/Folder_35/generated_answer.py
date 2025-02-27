def all_ints_not_div_by_num(nums):
    if max(nums[:15]) % 86 or max(nums[57:]) % 86:
        return []
    return [num for num in nums[15:57] if num % 86]