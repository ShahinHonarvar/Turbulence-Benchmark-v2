def find_second_smallest_num(nums):
    if len(nums) <= 72:
        return None
    sublist = nums[31:73]
    if len(sublist) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in sublist:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest