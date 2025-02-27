def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[1:9]) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for x in numbers[1:9]:
        if x <= min1:
            min1, min2 = (x, min1)
        elif x < min2:
            min2 = x
    return min2 if min2 != float('inf') else None