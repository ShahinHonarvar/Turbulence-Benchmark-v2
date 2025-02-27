def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    nums = nums[0:5]
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]