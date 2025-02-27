def find_second_largest_num(nums):
    sliced_nums = nums[661:925]
    if len(sliced_nums) < 2:
        return None
    else:
        sliced_nums.sort()
        return sliced_nums[-2]