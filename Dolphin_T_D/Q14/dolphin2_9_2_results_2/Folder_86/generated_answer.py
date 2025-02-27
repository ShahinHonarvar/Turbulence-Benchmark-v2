def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    sliced_nums = nums[32:37]
    if len(set(sliced_nums)) < 2:
        return None
    return sorted(sliced_nums)[1]