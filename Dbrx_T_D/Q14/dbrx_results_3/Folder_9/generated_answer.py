def find_second_smallest_num(nums):
    if len(nums) < 2 or (70 > len(nums) or 200 < len(nums)):
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for num in nums[70:201]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif min_num < num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None