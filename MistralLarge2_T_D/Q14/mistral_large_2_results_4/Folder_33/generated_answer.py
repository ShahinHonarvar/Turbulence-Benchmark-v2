def find_second_smallest_num(nums):
    if len(nums) < 747:
        return None
    sublist = nums[262:747]
    if len(sublist) < 2:
        return None
    first_min = second_min = float('inf')
    for num in sublist:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None