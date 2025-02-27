def find_second_smallest_num(nums):
    if len(nums) < 49:
        return None
    second_smallest = min(sorted(nums[30:49])[1:])
    return second_smallest if second_smallest != max(nums[30:49]) else None