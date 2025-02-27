def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    if nums[0] < nums[1]:
        return nums[1]
    elif nums[1] < nums[0]:
        return nums[0]
    else:
        return None