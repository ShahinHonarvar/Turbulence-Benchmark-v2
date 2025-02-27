def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    smallest_num = float('inf')
    second_smallest_num = float('inf')
    for num in nums[:6]:
        if num < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = num
        elif num < second_smallest_num:
            second_smallest_num = num
    return second_smallest_num if second_smallest_num != float('inf') else None