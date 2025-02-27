def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for i in range(8):
        if nums[i] < first_smallest:
            second_smallest = first_smallest
            first_smallest = nums[i]
        elif first_smallest < nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else None