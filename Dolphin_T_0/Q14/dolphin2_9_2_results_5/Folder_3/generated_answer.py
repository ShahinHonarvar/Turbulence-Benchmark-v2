def find_second_smallest_num(nums):
    subset = nums[27:56]
    if len(subset) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for n in subset:
        if n < min1:
            min1, min2 = (n, min1)
        elif n < min2 and n != min1:
            min2 = n
    return None if min2 == float('inf') else min2