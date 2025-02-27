def find_second_largest_num(nums):
    if len(nums) <= 200 or 100 >= len(nums):
        return None
    nums = nums[100:201]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]