def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        max_num = max(nums)
        nums.remove(max_num)
        return max(nums) if len(nums) else None