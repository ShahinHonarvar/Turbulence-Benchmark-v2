def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums = nums[:6]
    max_num = max(nums)
    nums.remove(max_num)
    if len(nums) < 2:
        return None
    second_max_num = max(nums)
    return second_max_num