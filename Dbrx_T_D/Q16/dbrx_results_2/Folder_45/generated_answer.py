def sum_even_ints_inclusive(numbers):
    start_index = 30
    end_index = 200
    if end_index < len(numbers):
        numbers = numbers[:end_index]
    if start_index > 0:
        numbers = numbers[start_index:]
    even_numbers = [num for num in numbers if num % 2 == 0]
    if len(even_numbers) == 0:
        return 0
    return sum(even_numbers)