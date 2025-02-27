def find_second_smallest_num(nums):
    if len(nums) == 0 or len(nums) < 2:
        return None
    a, b = (float('inf'), float('inf'))
    for num in nums[686:988]:
        if num <= a:
            a, b = (num, a)
        elif num < b:
            b = num
    return b if b != float('inf') else None