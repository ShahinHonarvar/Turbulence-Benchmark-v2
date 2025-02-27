def find_second_smallest_num(nums):
    if len(nums) == 0:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in nums[27:56]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        if num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None