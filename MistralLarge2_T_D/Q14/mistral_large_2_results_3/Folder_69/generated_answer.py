def find_second_smallest_num(nums):
    if len(nums) < 88:
        return None
    sublist = nums[25:88]
    if len(sublist) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None