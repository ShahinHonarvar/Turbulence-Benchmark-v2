def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first_min = float('inf')
    second_min = float('inf')
    for i in range(4):
        if nums[i] < first_min:
            second_min = first_min
            first_min = nums[i]
        elif first_min < nums[i] < second_min:
            second_min = nums[i]
    return second_min if second_min != float('inf') else None