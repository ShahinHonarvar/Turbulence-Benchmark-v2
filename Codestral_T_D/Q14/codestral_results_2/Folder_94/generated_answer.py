def find_second_smallest_num(nums):
    if 52 <= len(nums) <= 71:
        sorted_nums = sorted(nums[52:72])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None