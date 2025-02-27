def find_second_largest_num(numbers):
    if len(numbers) < 2 or index > 68 or index < 42:
        return None
    first, second = (None, None)
    for i in range(42, 69):
        if first is None or numbers[i] > first:
            first, second = (numbers[i], first)
        elif numbers[i] > second and numbers[i] < first:
            second = numbers[i]
    return second