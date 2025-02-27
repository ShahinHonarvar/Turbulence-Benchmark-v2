def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 66 or len(numbers) < 56:
        return None
    min1 = float('inf')
    min2 = float('inf')
    for num in numbers[56:67]:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    if min2 == float('inf'):
        return None
    else:
        return min2