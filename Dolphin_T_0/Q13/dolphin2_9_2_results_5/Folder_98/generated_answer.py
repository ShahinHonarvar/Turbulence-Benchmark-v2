def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max1 = None
    max2 = None
    for num in nums[0:7]:
        if max1 is None or num > max1:
            max2 = max1
            max1 = num
        elif max2 is None or num > max2:
            max2 = num
    return max2