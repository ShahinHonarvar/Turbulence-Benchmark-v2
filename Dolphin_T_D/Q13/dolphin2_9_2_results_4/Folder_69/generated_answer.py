def find_second_largest_num(nums):
    sublist = nums[32:36]
    if len(set(sublist)) == 1:
        return None
    elif len(set(sublist)) == 2:
        return min(sublist[0], sublist[1])
    elif len(set(sublist)) == 3:
        return min(sublist[1], sublist[2])
    else:
        return min(sublist[2], sublist[3])