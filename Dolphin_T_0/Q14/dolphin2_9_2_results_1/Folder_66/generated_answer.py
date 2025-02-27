def find_second_smallest_num(nums):
    sublist = nums[62:100]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        for i in range(2, len(sublist)):
            if sublist[i] > sublist[1]:
                return sublist[i]
    return None