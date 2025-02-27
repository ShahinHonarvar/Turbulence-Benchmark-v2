def find_second_largest_num(nums):
    if not nums:
        return None
    max_num = float('-inf')
    second_max = float('-inf')
    for num in nums[15:52]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None