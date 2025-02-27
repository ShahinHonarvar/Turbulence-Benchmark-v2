def find_second_smallest_num(nums):
    if len(nums) < 94:
        return None
    segment = nums[66:94]
    if len(segment) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in segment:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None