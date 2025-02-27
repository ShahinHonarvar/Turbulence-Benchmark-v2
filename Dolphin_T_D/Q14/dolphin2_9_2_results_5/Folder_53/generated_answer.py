def find_second_smallest_num(nums):
    valid_nums = [num for idx, num in enumerate(nums) if 1 <= idx <= 100]
    if len(valid_nums) < 2:
        return None
    else:
        sorted_nums = sorted(valid_nums)
        return sorted_nums[1]