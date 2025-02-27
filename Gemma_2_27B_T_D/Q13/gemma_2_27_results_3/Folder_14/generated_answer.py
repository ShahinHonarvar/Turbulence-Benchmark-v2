def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    temp = nums[5:8]
    temp.sort()
    if len(temp) < 2:
        return None
    return temp[-2]