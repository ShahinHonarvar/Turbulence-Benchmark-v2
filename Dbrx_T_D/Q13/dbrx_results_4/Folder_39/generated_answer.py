def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 30 - 20 + 1:
        return None
    unique_numbers = list(set(numbers[20:31]))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]