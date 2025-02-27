def find_second_largest_num(nums):
    if not nums:
        return None
    nums = nums[667:775]
    if len(nums) < 2:
        return None
    first = nums[0]
    second = None
    for num in nums[1:]:
        if num > first:
            first, second = (num, first)
        elif num != first and second is None or num > second:
            second = num
    if second is None:
        return None
    return second