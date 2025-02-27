def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 746 or len(numbers) - 262 < 2:
        return None
    min1 = min2 = float('inf')
    for num in numbers[262:747]:
        if num < min1:
            min1, min2 = (num, min1)
        elif min1 < num < min2:
            min2 = num
    if min2 == float('inf'):
        return None
    else:
        return min2