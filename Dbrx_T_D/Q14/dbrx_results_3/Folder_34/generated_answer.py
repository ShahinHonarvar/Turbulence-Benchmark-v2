def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 60:
        return None
    min1 = float('inf')
    min2 = float('inf')
    for i in range(60, 201):
        if numbers[i] <= min1:
            min2 = min1
            min1 = numbers[i]
        elif numbers[i] < min2 and numbers[i] > min1:
            min2 = numbers[i]
    if min2 == float('inf'):
        return None
    else:
        return min2