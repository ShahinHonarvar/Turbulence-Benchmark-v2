def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    else:
        sl = sorted(nums[5:8])
        if len(sl) < 2:
            return None
        else:
            return sl[1]