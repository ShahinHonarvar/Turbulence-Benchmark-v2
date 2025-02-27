def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = nums[23]
    second_smallest = None
    for num in nums[23:]:
        if second_smallest and num < second_smallest:
            second_smallest = num
        elif num < smallest and num != second_smallest:
            second_smallest = smallest
            smallest = num
    return second_smallest or None