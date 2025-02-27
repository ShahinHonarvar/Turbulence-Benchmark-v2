def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 88 or 75 > 88:
        return None
    min1 = float('inf')
    min2 = float('inf')
    for i in range(75, 89):
        if numbers[i] <= min1:
            min2 = min1
            min1 = numbers[i]
        elif numbers[i] < min2:
            min2 = numbers[i]
    return min2 if min2 != float('inf') else None