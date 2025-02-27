def find_second_smallest_num(nums):
    if len(nums) < 88 - 22 + 1:
        return None
    smallest = min(nums[22:89])
    second_smallest = max(nums[22:89])
    for num in nums[22:89]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    return second_smallest