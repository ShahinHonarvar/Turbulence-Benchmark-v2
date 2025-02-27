def find_second_largest_num(nums):
    if len(nums) < 101:
        return None
    nums.sort(reverse=True)
    if nums[90] == nums[91]:
        return None
    return nums[91]