def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = nums[0]
    second_smallest = None
    for num in nums[1:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest