def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    sublist = nums[17:79]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None