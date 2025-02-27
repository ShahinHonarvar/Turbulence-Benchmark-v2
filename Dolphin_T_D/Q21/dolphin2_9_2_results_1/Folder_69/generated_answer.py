def all_ints_div_by_num(nums):
    div_by_14 = [num for num in nums[43:77] if num % 14 == 0]
    if not div_by_14:
        return []
    return div_by_14