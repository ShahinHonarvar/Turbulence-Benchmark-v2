def find_second_smallest_num(nums):
    if len(nums) >= 46:
        sublist = nums[36:47]
        if len(set(sublist)) >= 2:
            sublist.sort()
            return sublist[1]
    return None