def find_second_smallest_num(nums):
    sublist = nums[22:51]
    if len(sublist) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for num in sublist:
        if num < first_min:
            second_min, first_min = (first_min, num)
        elif first_min < num < second_min:
            second_min = num
    return None if second_min == float('inf') else second_min