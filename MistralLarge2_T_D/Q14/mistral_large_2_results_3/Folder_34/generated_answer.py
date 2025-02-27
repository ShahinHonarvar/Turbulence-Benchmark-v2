def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    sublist = nums[60:201]
    if len(sublist) < 2:
        return None
    unique_nums = sorted(set(sublist))
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]