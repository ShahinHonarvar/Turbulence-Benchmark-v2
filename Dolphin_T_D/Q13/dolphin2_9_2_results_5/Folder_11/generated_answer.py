def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max1, max2 = (None, None)
    for i in range(37, 52):
        if nums[i] == None:
            continue
        if max1 == None or nums[i] > max1:
            max2 = max1
            max1 = nums[i]
        elif max1 != nums[i] and (max2 == None or nums[i] > max2):
            max2 = nums[i]
    return max2