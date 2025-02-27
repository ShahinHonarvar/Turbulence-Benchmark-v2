def find_second_smallest_num(nums):
    if len(nums) < 72:
        return None
    second_smallest = min(nums[52:72])
    nums[52:72].remove(second_smallest)
    if len(nums[52:72]) > 0:
        return min(nums[52:72])
    else:
        return None