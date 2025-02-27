def find_second_smallest_num(nums):
    if len(nums) < 81 or len(set(nums)) != len(nums):
        return None
    second_smallest = min(nums[40:81])
    smallest = min(nums[40:81])
    for num in nums[40:81]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    return second_smallest