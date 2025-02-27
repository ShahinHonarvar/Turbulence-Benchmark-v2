def find_second_largest_num(nums):
    if len(nums) < 2 or 639 > len(nums) or 975 > len(nums):
        return None
    else:
        sublist = nums[639:976]
        if len(sublist) < 2:
            return None
        else:
            max_num = max(sublist)
            sublist.remove(max_num)
            second_max_num = max(sublist)
            return second_max_num