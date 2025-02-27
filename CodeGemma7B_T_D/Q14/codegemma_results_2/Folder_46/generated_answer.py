def find_second_smallest_num(nums):
    if not nums:
        return None
    nums.sort()
    if len(nums) < 14 or nums[13] > nums[-69]:
        return None
    return nums[14]