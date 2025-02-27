def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    temp = nums[31:35]
    temp.sort()
    if len(temp) == 1:
        return None
    return temp[-2]