def find_second_smallest_num(nums):
    if 924 < len(nums) and len(nums) > 661:
        nums_slice = sorted(nums[661:925])
        if len(nums_slice) > 1:
            return nums_slice[1]
    return None