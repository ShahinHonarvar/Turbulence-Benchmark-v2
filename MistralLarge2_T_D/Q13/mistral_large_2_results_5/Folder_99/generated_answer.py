def find_second_largest_num(nums):
    if not nums or len(nums) < 371:
        return None
    subset = nums[310:371]
    if len(subset) < 2:
        return None
    max1, max2 = (float('-inf'), float('-inf'))
    for num in subset:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max2 if max2 != float('-inf') else None