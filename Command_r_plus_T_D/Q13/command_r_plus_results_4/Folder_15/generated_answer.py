def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    else:
        nums_slice = sorted(nums[:4])
        if len(nums_slice) < 2:
            return None
        else:
            return nums_slice[-2]