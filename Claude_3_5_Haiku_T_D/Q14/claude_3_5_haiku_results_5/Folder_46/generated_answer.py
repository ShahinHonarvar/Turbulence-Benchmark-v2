def find_second_smallest_num(nums):
    if len(nums) < 14:
        return None
    slice_nums = nums[13:69]
    if not slice_nums:
        return None
    try:
        smallest = min(slice_nums)
        slice_nums.remove(smallest)
        return min(slice_nums)
    except ValueError:
        return None