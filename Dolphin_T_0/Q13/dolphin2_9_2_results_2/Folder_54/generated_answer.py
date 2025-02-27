def find_second_largest_num(numbers):
    if 34 <= len(numbers) <= 55:
        numbers = numbers[34:56]
        unique_numbers = list(set(numbers))
        unique_numbers.sort()
        if len(unique_numbers) > 1:
            return unique_numbers[-2]
    return None