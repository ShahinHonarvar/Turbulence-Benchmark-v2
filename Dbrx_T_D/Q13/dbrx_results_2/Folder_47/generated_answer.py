def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 76 or (not all((isinstance(i, (int, float)) for i in numbers))):
        return None
    first, second = max(numbers[37:77])
    for num in numbers[37:77]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return None if second == first else second