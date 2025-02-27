def find_second_smallest_num(nums):
    nums.sort()
    return nums[74:95][1] if len(nums[74:95]) >= 2 else 'None'