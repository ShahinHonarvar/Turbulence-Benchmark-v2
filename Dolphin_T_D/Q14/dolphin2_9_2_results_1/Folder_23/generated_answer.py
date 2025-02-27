def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in numbers:
        if num < min1:
            min1, min2 = (num, min1)
        elif num < min2 and num != min1:
            min2 = num
    if min2 == float('inf'):
        return None
    return min2