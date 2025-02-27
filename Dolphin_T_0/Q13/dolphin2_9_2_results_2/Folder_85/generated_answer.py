def find_second_largest_num(nums):
    sublist = nums[6:9]
    if len(set(sublist)) < 2:
        return None
    else:
        return sorted(sublist)[-2]