def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 62 or any((not isinstance(num, (int, float)) for num in numbers)):
        return None
    unique_numbers = list(set(numbers[15:61]))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]