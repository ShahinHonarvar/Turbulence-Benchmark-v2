def find_second_smallest_num(nums):
    if len(nums) < 3 or max(nums) <= nums[3] or max(nums) <= nums[5]:
        return None
    nums_sub = nums[3:6]
    nums_sub.sort()
    return nums_sub[1]