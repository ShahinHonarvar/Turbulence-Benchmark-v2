def find_second_smallest_num(nums):
    if len(nums) < 51:
        return None
    sliced_nums = nums[22:51]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]