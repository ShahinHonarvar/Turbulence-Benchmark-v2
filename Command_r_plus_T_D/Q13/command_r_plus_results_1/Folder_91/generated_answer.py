def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    else:
        nums = sorted(nums[:6])
        if len(nums) < 2:
            return None
        else:
            return nums[-2]