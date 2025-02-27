def find_second_smallest_num(nums):
    sublist = nums[74:96]
    if len(sublist) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in sublist:
        if num <= min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    if min2 == float('inf'):
        return None
    return min2