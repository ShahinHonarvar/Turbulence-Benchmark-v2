def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max1 = max2 = float('-inf')
    for num in nums[:9]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max2 if max2 != float('-inf') else None