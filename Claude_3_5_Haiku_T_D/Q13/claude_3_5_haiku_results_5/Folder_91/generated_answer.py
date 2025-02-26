def find_second_largest_num(nums):
    if len(nums) <= 1 or len(nums) < 6:
        return None
    sublist = nums[0:6]
    largest = max(sublist)
    second_largest = None
    for num in sublist:
        if num > second_largest and num != largest:
            second_largest = num
    return second_largest