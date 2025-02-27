def find_second_smallest_num(nums):
    if len(nums[37:77]) < 2:
        return None
    smallest, second_smallest = (float('inf'), float('inf'))
    for num in nums[37:77]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest