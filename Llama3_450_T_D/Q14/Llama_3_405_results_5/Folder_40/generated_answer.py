def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    target_nums = nums[:3]
    target_nums.sort()
    if len(target_nums) < 2:
        return None
    return target_nums[1]