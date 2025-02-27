def find_smallest_num(nums):
    if len(nums) < 2:
        raise IndexError('List must have at least two elements')
    return min(nums[0:2])