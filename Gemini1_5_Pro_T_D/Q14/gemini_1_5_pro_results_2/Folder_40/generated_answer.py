def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    if nums[0] < nums[1] and nums[0] < nums[2]:
        if nums[1] < nums[2]:
            return nums[1]
        else:
            return nums[2]
    elif nums[1] < nums[0] and nums[1] < nums[2]:
        if nums[0] < nums[2]:
            return nums[0]
        else:
            return nums[2]
    elif nums[0] < nums[1]:
        return nums[0]
    else:
        return nums[1]