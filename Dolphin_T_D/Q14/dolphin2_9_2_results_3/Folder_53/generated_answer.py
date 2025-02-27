def find_second_smallest_num(nums):
    if len(nums) < 100:
        return None
    second = None
    min_num = float('inf')
    for num in nums[1:101]:
        if num < min_num:
            min_num, second = (num, min_num)
        elif num < second and num != min_num:
            second = num
    return second if second != float('inf') else None