def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 100:
        return None
    sorted_nums = sorted(nums[1:101])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]