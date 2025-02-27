def find_second_largest_num(nums):
    if len(nums) < 94 or len(nums[29:94]) < 2:
        return None
    sub_nums = nums[29:94]
    largest = max(sub_nums)
    second_largest = min(sub_nums)
    for num in sub_nums:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest