def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first = max(nums[0], nums[1])
    second = min(nums[0], nums[1])
    for i in range(2, min(4, len(nums))):
        if nums[i] > first:
            second = first
            first = nums[i]
        elif nums[i] > second and nums[i] != first:
            second = nums[i]
    if second != first:
        return second
    else:
        return None