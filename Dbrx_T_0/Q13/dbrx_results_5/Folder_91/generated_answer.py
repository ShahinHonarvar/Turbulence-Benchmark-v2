def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    first, second = (max(numbers[0], numbers[1]), min(numbers[0], numbers[1]))
    for num in numbers[2:6]:
        if num > first:
            first, second = (num, first)
        elif num > second and num != first:
            second = num
    return second if second != first else None