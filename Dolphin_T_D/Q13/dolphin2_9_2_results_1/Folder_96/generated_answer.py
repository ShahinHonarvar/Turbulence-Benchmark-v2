def find_second_largest_num(nums):
    if not nums[15:52]:
        return None
    max_num = nums[15]
    second_max_num = None
    for i in range(16, len(nums) + 1):
        if nums[i] > max_num:
            second_max_num = max_num
            max_num = nums[i]
        elif nums[i] < max_num and nums[i] > second_max_num:
            second_max_num = nums[i]
    return second_max_num if second_max_num else None