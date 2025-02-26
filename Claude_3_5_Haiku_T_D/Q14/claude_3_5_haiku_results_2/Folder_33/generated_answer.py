def find_second_smallest_num(nums):
    if not nums or len(nums) <= 262:
        return None
    slice_nums = nums[262:747]
    if len(slice_nums) < 2:
        return None
    first_smallest = min(slice_nums)
    second_smallest = float('inf')
    for num in slice_nums:
        if num < second_smallest and num > first_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None