def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 55 or (not all((isinstance(num, (int, float)) for num in numbers))):
        return None
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    second_largest = unique_numbers[1]
    return second_largest