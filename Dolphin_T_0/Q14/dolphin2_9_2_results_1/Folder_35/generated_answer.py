def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    min1 = min(nums)
    nums.remove(min1)
    min2 = min(nums)
    return min2