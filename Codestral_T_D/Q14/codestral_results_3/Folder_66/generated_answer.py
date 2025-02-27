def find_second_smallest_num(nums):
    sublist = sorted(nums[62:100])
    if len(sublist) > 1:
        return sublist[1]
    return None