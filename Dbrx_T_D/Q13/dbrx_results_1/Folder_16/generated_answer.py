def find_second_largest_num(numbers):
    if len(numbers) < 2 or any((not isinstance(num, (int, float)) for num in numbers)):
        return None
    numbers = sorted(numbers)[33:37]
    largest, second_largest = (max(numbers), max((num for num in numbers if num < largest)))
    return second_largest if largest != second_largest else None