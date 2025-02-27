def find_second_smallest_num(nums):
    if not nums or len(nums) < 750:
        return None
    sublist = nums[246:751]
    unique_nums = list(set(sublist))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[1]