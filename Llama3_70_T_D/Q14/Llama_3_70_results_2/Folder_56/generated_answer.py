def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min_num = second_min_num = float('inf')
    for num in nums:
        if num <= min_num:
            second_min_num = min_num
            min_num = num
        elif num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None