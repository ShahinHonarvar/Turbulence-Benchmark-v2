def find_second_largest_num(nums):
    if len(nums) < 775:
        return None
    sublist = nums[667:775]
    unique_nums = list(set(sublist))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]