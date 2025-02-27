def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = max(nums)
    if nums.count(max_num) > 1:
        nums.remove(max_num)
    second_max = max(nums)
    if nums[62:100].count(second_max) > 1:
        nums[62:100].remove(second_max)
    return second_max if nums[62:100] else None