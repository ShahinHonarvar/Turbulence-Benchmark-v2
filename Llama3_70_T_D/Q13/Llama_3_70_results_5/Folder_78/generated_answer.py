def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    else:
        nums_slice = sorted(set(nums[43:52]), reverse=True)
        if len(nums_slice) < 2:
            return None
        else:
            return nums_slice[1]