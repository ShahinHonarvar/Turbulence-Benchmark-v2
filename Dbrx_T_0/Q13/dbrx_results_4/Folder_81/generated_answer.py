def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 101 or (not all((isinstance(i, (int, float)) for i in numbers))):
        return None
    unique_numbers = list(set(numbers[10:101]))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]