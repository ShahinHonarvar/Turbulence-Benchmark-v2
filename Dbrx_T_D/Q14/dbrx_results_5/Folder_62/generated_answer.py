def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    min_2nd = float('inf')
    min_1st = float('inf')
    for i in range(10, 67):
        if numbers[i] < min_2nd:
            if numbers[i] < min_1st:
                min_2nd = min_1st
                min_1st = numbers[i]
            elif numbers[i] > min_1st and numbers[i] < min_2nd:
                min_2nd = numbers[i]
    if min_2nd == float('inf'):
        return None
    else:
        return min_2nd