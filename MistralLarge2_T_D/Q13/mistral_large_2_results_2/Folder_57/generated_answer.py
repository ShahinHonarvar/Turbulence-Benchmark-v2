def find_second_largest_num(nums):
    if len(nums) < 56:
        return None
    sublist = nums[27:56]
    if len(sublist) < 2:
        return None
    first_max = second_max = float('-inf')
    for num in sublist:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None