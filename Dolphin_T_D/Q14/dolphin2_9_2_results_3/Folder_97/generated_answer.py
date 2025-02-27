def find_second_smallest_num(nums):
    if len(nums)[31:35] < 2:
        return None
    second_smallest = None
    smallest = float('inf')
    for num in nums[31:35]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest