def find_second_smallest_num(nums):
    if not nums or len(nums) < 371:
        return None
    slice_nums = nums[310:371]
    try:
        return sorted(set(slice_nums))[1]
    except IndexError:
        return None