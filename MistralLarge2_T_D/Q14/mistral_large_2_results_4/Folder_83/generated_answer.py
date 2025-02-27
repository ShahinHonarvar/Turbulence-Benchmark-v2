def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    subset = nums[90:201]
    if len(subset) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in subset:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None