def find_second_smallest_num(nums):
    if len(nums) <= 1 or len(nums) <= 9:
        return None
    first, second = (float('inf'), float('inf'))
    for num in nums[0:10]:
        if num <= first:
            first, second = (num, first)
        elif num < second:
            second = num
    return None if second == float('inf') else second