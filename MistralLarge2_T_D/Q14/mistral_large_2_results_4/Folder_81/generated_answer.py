def find_second_smallest_num(nums):
    subset = nums[10:101]
    if len(subset) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in subset:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None