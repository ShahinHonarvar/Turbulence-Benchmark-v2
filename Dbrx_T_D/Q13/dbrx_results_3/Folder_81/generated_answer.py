def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 101:
        return None
    second_largest = None
    largest = float('-inf')
    for num in numbers[10:101]:
        if largest < num:
            second_largest, largest = (largest, num)
        elif second_largest < num < largest:
            second_largest = num
    return second_largest if second_largest != largest else None