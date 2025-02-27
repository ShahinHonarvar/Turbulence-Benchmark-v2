def find_second_smallest_num(nums):
    if not nums[29:94]:
        return None
    sorted_nums = sorted(nums[29:94])
    return sorted_nums[1] if len(sorted_nums) > 1 else None