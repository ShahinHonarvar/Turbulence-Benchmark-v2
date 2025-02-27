def find_second_smallest_num(nums):
    if 8 <= len(nums) <= 9:
        sorted_nums = sorted(nums[8:10])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    return None