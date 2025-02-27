def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    elif nums[0] > nums[1]:
        return nums[1]
    else:
        return nums[0]