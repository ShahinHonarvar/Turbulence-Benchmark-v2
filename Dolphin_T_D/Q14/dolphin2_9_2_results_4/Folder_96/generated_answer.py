def find_second_smallest_num(nums):
    if len(nums) < 200:
        return None
    sub_nums = nums[50:201]
    smallest = smallest = second_smallest = float('inf')
    for num in sub_nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        if smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest