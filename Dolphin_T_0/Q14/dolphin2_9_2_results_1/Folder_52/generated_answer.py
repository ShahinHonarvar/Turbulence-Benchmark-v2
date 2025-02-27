def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    nums = nums[64:67]
    nums.sort()
    return nums[1] if nums[1] != nums[2] else None