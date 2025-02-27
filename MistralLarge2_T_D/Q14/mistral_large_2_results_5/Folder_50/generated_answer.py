def find_second_smallest_num(nums):
    if len(nums) < 69:
        return None
    sublist = nums[42:69]
    unique_nums = sorted(set(sublist))
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]