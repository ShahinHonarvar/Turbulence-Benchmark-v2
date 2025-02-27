def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 8:
        return None
    first, second = (max(numbers[0], numbers[7]), min(numbers[0], numbers[7]))
    for i in range(1, 7):
        if numbers[i] > first:
            first, second = (numbers[i], first)
        elif numbers[i] > second and numbers[i] != first:
            second = numbers[i]
    return second if second != first else None