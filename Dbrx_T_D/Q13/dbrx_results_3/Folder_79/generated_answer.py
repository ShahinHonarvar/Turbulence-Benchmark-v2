def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        numbers = numbers[4:5]
    first, second = (max(numbers) if len(numbers) > 1 else None, max((num for num in numbers if num < first)) if len(numbers) > 2 else None)
    return second