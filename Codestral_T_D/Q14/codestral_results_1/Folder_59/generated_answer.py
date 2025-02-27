def find_second_smallest_num(nums):
    if len(nums) <= 1 or len(nums) <= 9:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for i in range(10):
        if nums[i] < min1:
            min1, min2 = (nums[i], min1)
        elif nums[i] < min2 and nums[i] != min1:
            min2 = nums[i]
    return None if min2 == float('inf') else min2