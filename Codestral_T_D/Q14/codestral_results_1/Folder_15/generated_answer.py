def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    first_smallest = min(nums[0:4])
    nums[nums.index(first_smallest)] = float('inf')
    second_smallest = min(nums[0:4])
    if second_smallest == float('inf'):
        return None
    return second_smallest