def find_second_smallest_num(nums):
    if len(nums) < 89:
        return None
    temp = sorted(nums[75:89])
    if len(temp) < 2:
        return None
    return temp[1]