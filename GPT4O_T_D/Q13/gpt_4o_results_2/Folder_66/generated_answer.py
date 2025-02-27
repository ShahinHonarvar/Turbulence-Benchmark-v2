def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    sliced_numbers = numbers[50:55]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]