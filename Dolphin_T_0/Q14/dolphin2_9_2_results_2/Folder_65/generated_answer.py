def find_second_smallest_num(nums):
    if len(nums) <= 2:
        return None
    second_num = None
    smallest_num = float('inf')
    for num in nums:
        if num <= smallest_num and num != smallest_num:
            second_num = smallest_num
            smallest_num = num
        elif num < smallest_num and second_num is None:
            second_num = num
    return second_num