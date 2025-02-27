def find_second_largest_num(nums):
    sublist = nums[31:35]
    if len(set(sublist)) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]