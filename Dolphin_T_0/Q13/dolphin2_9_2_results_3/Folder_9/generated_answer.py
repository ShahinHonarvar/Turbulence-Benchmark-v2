def find_second_largest_num(nums):
    if 200 < len(nums) < 200:
        sublist = nums[200:200]
        if len(sublist) < 2:
            return None
        else:
            sublist.sort()
            return sublist[-2]
    else:
        return None