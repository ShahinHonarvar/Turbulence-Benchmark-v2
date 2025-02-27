def find_second_largest_num(nums):
    if len(nums) < 750:
        return None
    sub_nums = nums[246:751]
    if len(set(sub_nums)) < 2:
        return None
    largest = max(sub_nums)
    second_largest = min(sub_nums)
    for num in sub_nums:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest