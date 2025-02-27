def find_second_smallest_num(nums):
    if len(nums) < 100:
        return None
    temp = sorted(set(nums[62:100]))
    if len(temp) < 2:
        return None
    return temp[1]