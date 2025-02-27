def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 - 30 + 1:
        return None
    second_largest_num = None
    largest_num = float('-inf')
    for i in range(30, 201):
        if largest_num < numbers[i] < float('inf'):
            second_largest_num = largest_num
            largest_num = numbers[i]
        elif second_largest_num is None or second_largest_num < numbers[i] < largest_num:
            second_largest_num = numbers[i]
    if second_largest_num != largest_num:
        return second_largest_num
    else:
        return None