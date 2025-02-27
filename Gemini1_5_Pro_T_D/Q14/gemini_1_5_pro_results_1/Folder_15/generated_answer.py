def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first_smallest = nums[0]
    second_smallest = nums[1]
    if second_smallest < first_smallest:
        first_smallest, second_smallest = (second_smallest, first_smallest)
    for i in range(2, min(4, len(nums))):
        if nums[i] < first_smallest:
            first_smallest, second_smallest = (nums[i], first_smallest)
        elif nums[i] < second_smallest and nums[i] != first_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != first_smallest else None