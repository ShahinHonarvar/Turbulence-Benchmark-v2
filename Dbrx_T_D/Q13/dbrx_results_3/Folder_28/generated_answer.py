def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first, second = (float('-inf'), float('-inf'))
    for i in range(62, 64):
        if numbers[i] > first:
            first, second = (numbers[i], first)
        elif numbers[i] > second and numbers[i] != first:
            second = numbers[i]
    if first == second:
        return None
    else:
        return second