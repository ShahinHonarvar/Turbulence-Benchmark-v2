def find_second_smallest_num(nums):
    if not nums:
        return None
    second_smallest_num = None
    smallest_num = None
    for num in nums:
        if smallest_num is None and num >= nums[30]:
            smallest_num = num
        elif smallest_num is not None and second_smallest_num is None and (num != smallest_num) and (num > smallest_num) and (num >= nums[30]):
            second_smallest_num = num
    return second_smallest_num