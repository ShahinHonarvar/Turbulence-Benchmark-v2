def find_second_smallest_num(nums):
    sublist = sorted(nums[6:9])
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None