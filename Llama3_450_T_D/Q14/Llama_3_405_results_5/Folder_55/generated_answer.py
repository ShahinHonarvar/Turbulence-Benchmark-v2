def find_second_smallest_num(nums):
    if len(nums) < 2 or 10 >= len(nums):
        return None
    target_nums = nums[10:11]
    if len(target_nums) < 2:
        return None
    target_nums.sort()
    return target_nums[1]