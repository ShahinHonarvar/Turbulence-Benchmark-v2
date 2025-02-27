def find_second_smallest_num(nums):
    if len(nums) <= 100:
        subset = nums[10:]
    else:
        subset = nums[10:101]
    if len(subset) < 2:
        return None
    first_min = second_min = float('inf')
    for num in subset:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
    if second_min == float('inf'):
        return None
    return second_min