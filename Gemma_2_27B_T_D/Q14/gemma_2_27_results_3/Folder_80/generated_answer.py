def find_second_smallest_num(nums):
    if len(nums) < 58 or len(set(nums)) != len(nums):
        return None
    trimmed_nums = nums[30:88]
    trimmed_nums.sort()
    return trimmed_nums[1]