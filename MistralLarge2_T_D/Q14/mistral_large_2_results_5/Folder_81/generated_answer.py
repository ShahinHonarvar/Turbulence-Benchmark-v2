def find_second_smallest_num(nums):
    if len(nums) <= 100:
        sublist = nums[10:]
    else:
        sublist = nums[10:101]
    unique_nums = sorted(set(sublist))
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]