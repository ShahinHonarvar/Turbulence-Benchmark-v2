def find_second_smallest_num(nums):
    if len(nums) < 35:
        return None
    else:
        sl = sorted(nums[31:35])
        if len(sl) < 2:
            return None
        else:
            return sl[1]