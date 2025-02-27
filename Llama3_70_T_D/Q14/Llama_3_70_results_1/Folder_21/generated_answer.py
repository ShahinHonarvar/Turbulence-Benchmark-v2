def find_second_smallest_num(nums):
    if 661 >= len(nums) or 924 >= len(nums):
        return None
    nums_slice = sorted(nums[661:925])
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]