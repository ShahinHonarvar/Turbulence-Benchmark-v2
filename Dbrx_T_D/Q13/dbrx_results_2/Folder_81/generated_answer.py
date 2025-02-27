def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 100 or len(numbers) < 10:
        return None
    first_part = numbers[10:101]
    unique_numbers = list(set(first_part))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]