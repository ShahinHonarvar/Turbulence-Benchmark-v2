def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    sorted_nums = sorted(nums[1:6])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]