def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in nums:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None