def find_second_smallest_num(nums):
    if len(nums) <= 76:
        sublist = nums[37:77]
    else:
        sublist = nums[37:76]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return None if second == float('inf') else second