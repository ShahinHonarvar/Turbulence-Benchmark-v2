def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums = nums[90:91]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return nums[1]