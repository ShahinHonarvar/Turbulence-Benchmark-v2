def find_second_largest_num(nums):
    temp = sorted(nums[6:7])
    if len(temp) < 2:
        return None
    return temp[-2]