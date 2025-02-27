def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in numbers[25:60]:
        if num < min1:
            min1, min2 = (num, min1)
        elif num < min2 and num > min1:
            min2 = num
    return min2 if min2 != float('inf') else None