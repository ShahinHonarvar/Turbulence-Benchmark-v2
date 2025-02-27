def find_second_smallest_num(nums):
    if len(nums) < 88:
        return None
    subset = nums[25:88]
    if len(subset) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for num in subset:
        if num < first_min:
            second_min, first_min = (first_min, num)
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None