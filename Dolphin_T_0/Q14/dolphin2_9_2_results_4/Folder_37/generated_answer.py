def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    else:
        sublist = nums[5:8]
        if len(set(sublist)) == 1:
            return None
        else:
            sublist.sort()
            return sublist[1]