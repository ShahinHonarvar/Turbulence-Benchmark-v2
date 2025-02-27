def find_second_smallest_num(lst):
    if len(lst) < 55:
        return None
    nums = lst[55:98]
    if len(nums) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in nums:
        if num <= smallest:
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest