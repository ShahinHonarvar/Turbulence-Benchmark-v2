def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for n in nums[:6]:
        if n < min_num:
            min_num, second_min_num = (n, min_num)
        elif n < second_min_num and n != min_num:
            second_min_num = n
    if second_min_num == float('inf'):
        return None
    return second_min_num