def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    elif nums[0] > nums[1] and (len(nums) == 2 or nums[0] > nums[2]):
        return nums[1]
    elif len(nums) == 2 or nums[1] > nums[2]:
        return nums[2]
    else:
        return nums[0]