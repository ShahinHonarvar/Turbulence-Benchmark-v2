def find_second_largest_num(numbers):
    if len(numbers) < 5 or not all((isinstance(num, (int, float)) for num in numbers)):
        return None
    target_numbers = set(numbers[3:6])
    target_numbers.discard(min(target_numbers))
    if len(target_numbers) == 1:
        return max(target_numbers)
    return None