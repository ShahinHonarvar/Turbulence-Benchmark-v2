def find_second_largest_num(nums):
    if 200 < len(nums) <= 201:
        return None
    slice_nums = nums[200:201]
    if len(slice_nums) != 2:
        return None
    largest = max(slice_nums)
    slice_nums.remove(largest)
    return max(slice_nums)