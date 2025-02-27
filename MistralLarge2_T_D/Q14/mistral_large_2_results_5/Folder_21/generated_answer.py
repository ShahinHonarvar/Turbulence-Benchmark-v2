def find_second_smallest_num(nums):
    if len(nums) < 925:
        return None
    slice_nums = nums[661:925]
    if len(slice_nums) < 2:
        return None
    sorted_nums = sorted(slice_nums)
    return sorted_nums[1]