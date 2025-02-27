def find_second_smallest_num(nums):
    if len(nums) < 46 or nums[35] == nums[36]:
        return None
    sublist = nums[36:47]
    return sorted(set(sublist))[1]