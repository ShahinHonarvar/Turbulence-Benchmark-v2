def find_second_largest_num(nums):
    if not nums:
        return None
    nums = sorted(nums)
    if len(nums) <= 1:
        return None
    start_index = 661
    end_index = 924
    for i in range(start_index, end_index + 1):
        if i >= len(nums):
            return None
        if nums[i] > nums[-2]:
            return nums[-2]
    return None