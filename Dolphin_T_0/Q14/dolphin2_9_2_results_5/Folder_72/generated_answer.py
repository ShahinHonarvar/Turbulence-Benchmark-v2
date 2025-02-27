def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 6:
        return None
    sliced_nums = nums[82:87]
    min_num = min(sliced_nums)
    second_min = None
    for num in sliced_nums:
        if num != min_num and (second_min is None or num < second_min):
            second_min = num
    return second_min