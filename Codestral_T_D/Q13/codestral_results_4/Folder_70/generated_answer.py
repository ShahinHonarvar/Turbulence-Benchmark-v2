def find_second_largest_num(nums):
    sublist = nums[28:33]
    if len(sublist) < 2:
        return None
    max1, max2 = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > max1:
            max2 = max1
            max1 = num
        elif max1 > num > max2:
            max2 = num
    if max2 == float('-inf'):
        return None
    return max2