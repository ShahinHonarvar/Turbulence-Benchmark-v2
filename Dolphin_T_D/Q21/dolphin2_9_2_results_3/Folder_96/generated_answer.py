def all_ints_div_by_num(nums):
    if 20 < len(nums):
        return [num for num in nums[20:21] if num % 2 == 0]
    else:
        return []