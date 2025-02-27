def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (numbers[0], numbers[1]) if numbers[0] > numbers[1] else (numbers[1], numbers[0])
    for num in numbers[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num != first:
            second = num
    return second if second != first else None