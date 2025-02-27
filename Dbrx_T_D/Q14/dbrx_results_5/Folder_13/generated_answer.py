def find_second_smallest_num(numbers):
    if len(numbers) < 5 or len(numbers) > 1000 or (not all((isinstance(num, (int, float)) for num in numbers))):
        return None
    sorted_numbers = sorted(numbers[28:33])
    if len(sorted_numbers) < 2 or sorted_numbers.count(sorted_numbers[1]) != 1:
        return None
    else:
        return sorted_numbers[1]