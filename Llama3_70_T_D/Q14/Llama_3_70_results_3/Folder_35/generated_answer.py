def find_second_smallest_num(nums):
    if len(nums) < 40:
        return None
    second_smallest = min(nums[15:40])
    nums[15:40] = [x for x in nums[15:40] if x != second_smallest]
    second_smallest = min(nums[15:40]) if nums[15:40] else None
    return second_smallest