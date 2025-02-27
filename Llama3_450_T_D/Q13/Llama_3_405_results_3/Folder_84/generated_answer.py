def find_second_largest_num(nums):
    sliced_nums = nums[43:87]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort(reverse=True)
    return sliced_nums[1]