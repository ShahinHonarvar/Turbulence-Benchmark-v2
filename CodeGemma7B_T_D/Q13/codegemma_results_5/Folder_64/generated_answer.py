def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 5:
        return None
    nums.sort()
    index = len(nums) - 2
    if index >= 0:
        return nums[index]
    else:
        return None