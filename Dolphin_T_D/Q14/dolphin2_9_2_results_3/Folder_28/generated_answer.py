def find_second_smallest_num(nums):
    if 50 < len(nums) < 22:
        return None
    smallests = sorted(nums[22:51])
    if len(smallests) < 2:
        return None
    return smallests[1]