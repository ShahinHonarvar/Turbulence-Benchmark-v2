def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 5:
        return None
    first, second = (max(numbers[0], numbers[1]), min(numbers[0], numbers[1]))
    for i in range(2, 5):
        num = numbers[i]
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second if second != first else None