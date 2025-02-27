def find_second_largest_num(nums):
    if not nums[15:52]:
        return None
    sorted_nums = sorted(nums[15:52], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None