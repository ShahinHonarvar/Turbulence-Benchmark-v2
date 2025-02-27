def find_second_smallest_num(nums):
    subset = nums[56:99]
    if len(subset) < 2:
        return None
    first_min = second_min = float('inf')
    for num in subset:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None