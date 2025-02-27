def find_second_smallest_num(nums):
    if not nums or len(nums) < 41:
        return None
    sorted_nums = sorted(nums[40:81])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]