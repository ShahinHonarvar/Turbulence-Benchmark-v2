def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 83 or nums[55] == nums[82]:
        return None
    return nums[56]