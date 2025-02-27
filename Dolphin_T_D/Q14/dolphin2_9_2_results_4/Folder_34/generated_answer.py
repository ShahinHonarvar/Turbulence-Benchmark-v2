def find_second_smallest_num(numbers):
    if len(numbers) == 0 or len(numbers) < 2:
        return None
    min1 = min2 = float('inf')
    for i in range(60, 201):
        if numbers[i] < min1:
            min2 = min1
            min1 = numbers[i]
        elif numbers[i] < min2 and numbers[i] > min1:
            min2 = numbers[i]
    return min2 if min2 != float('inf') else None