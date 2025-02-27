def find_second_smallest_num(nums):
    if len(nums) < 56:
        return None
    else:
        second_smallest = min(nums[27:56])
        nums[27:56].remove(second_smallest)
        return min(nums[27:56]) if nums[27:56] else None