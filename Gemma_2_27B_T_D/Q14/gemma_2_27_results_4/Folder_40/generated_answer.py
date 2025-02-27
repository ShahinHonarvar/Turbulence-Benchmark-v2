def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    first_smallest = min(nums[0], nums[1], nums[2])
    second_smallest = max(nums[0], nums[1], nums[2])
    for i in range(3):
        if nums[i] != first_smallest and nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest