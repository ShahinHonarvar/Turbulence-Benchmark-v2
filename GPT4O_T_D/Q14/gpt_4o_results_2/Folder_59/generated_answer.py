def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    unique_nums = sorted(nums[0:10])
    return unique_nums[1] if len(unique_nums) > 1 else None