def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for i in numbers[56:58]:
        if i < min1:
            min2 = min1
            min1 = i
        elif min1 < i < min2:
            min2 = i
    return min2 if min2 != float('inf') else None