def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min1 = min(nums[0:7])
    nums.remove(min1)
    if len(nums) < 2:
        return None
    min2 = min(nums)
    return min2 if min2 != min1 else None