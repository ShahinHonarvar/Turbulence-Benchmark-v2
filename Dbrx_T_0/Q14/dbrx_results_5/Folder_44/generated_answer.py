def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 99 or 91 > len(numbers) - 1:
        return None
    min1 = float('inf')
    min2 = float('inf')
    for i in range(91, 100):
        if numbers[i] < min1:
            min2 = min1
            min1 = numbers[i]
        elif numbers[i] < min2 and numbers[i] != min1:
            min2 = numbers[i]
    if min2 == float('inf'):
        return None
    else:
        return min2