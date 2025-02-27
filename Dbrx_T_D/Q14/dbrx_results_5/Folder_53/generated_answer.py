def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for i in range(1, min(len(numbers), 101)):
        if numbers[i] <= min1:
            min2 = min1
            min1 = numbers[i]
        elif numbers[i] < min2:
            min2 = numbers[i]
    if min2 == float('inf'):
        return None
    else:
        return min2