def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    target_nums = sorted(nums[6:9])
    if len(target_nums) < 2:
        return None
    return target_nums[1]