def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first = second = float('inf')
    for i in range(min(4, len(nums))):
        if nums[i] < first:
            second = first
            first = nums[i]
        elif nums[i] < second and nums[i] != first:
            second = nums[i]
    if second == float('inf'):
        return None
    else:
        return second