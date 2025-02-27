def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 101 or (not all((isinstance(i, (int, float)) for i in numbers))):
        return None
    first_largest = second_largest = numbers[9]
    for num in numbers[10:101]:
        if first_largest < num:
            first_largest, second_largest = (num, first_largest)
        elif second_largest < num < first_largest:
            second_largest = num
    return second_largest if first_largest != second_largest else None