def find_second_largest_num(nums):
    sublist = nums[68:87]
    if len(sublist) < 2:
        return None
    else:
        maximum = first = float('-inf')
        second = float('-inf')
        for num in sublist:
            if num > maximum:
                first, maximum = (maximum, num)
            elif maximum > num > second:
                second = num
        return None if second == float('-inf') else second