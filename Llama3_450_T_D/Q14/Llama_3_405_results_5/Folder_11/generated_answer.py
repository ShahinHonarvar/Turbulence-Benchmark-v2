def find_second_smallest_num(nums):
    if len(nums) < 94:
        return None
    sliced_nums = nums[66:94]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort()
    return sliced_nums[1]