def find_second_largest_num(nums):
    temp = sorted(nums[62:93], reverse=True)
    if len(temp) < 2:
        return None
    return temp[1]