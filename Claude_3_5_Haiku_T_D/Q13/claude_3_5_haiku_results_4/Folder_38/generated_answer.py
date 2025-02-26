def find_second_largest_num(nums):
    if len(nums) < 64 or len(nums) < 23:
        return None
    sublist = nums[22:64]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = None
    for num in sublist:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest