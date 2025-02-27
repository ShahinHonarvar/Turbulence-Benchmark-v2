def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    nums = sorted(nums[80:201], reverse=True)
    if len(nums) < 2 or nums[0] == nums[1]:
        return None
    return nums[1]