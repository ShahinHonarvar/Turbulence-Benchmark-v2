def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for i in range(91, 100):
        if nums[i] < min1:
            min1, min2 = (nums[i], min1)
        elif nums[i] < min2:
            min2 = nums[i]
    return min2 if min2 != float('inf') else None