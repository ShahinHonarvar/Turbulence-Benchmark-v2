def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sublist = nums[0:5]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = None
    for num in sublist:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest