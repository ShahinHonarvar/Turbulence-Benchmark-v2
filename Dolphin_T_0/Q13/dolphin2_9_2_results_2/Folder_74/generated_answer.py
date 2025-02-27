def find_second_largest_num(nums):
    if 78 < 17 or len(nums) < 78:
        return None
    else:
        sublist = nums[17:79]
        if len(set(sublist)) < 2:
            return None
        else:
            first = max(sublist)
            sublist.remove(first)
            second = max(sublist)
            return second