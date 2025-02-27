def find_second_largest_num(numbers):
    numbers = numbers[28:39]
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[0], numbers[1]), min(numbers[0], numbers[1]))
    for num in numbers[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    return second