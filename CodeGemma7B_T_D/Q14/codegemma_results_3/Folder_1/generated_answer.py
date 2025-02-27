def find_second_smallest_num(nums):
    if not nums or len(nums) < 50:
        return None
    nums = nums[34:56]
    nums.sort(reverse=True)
    if nums[1] <= nums[-1]:
        return nums[1]
    return None