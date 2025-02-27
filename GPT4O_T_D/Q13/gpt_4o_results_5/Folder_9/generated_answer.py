def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 200:
        return None
    sliced_numbers = numbers[200:201]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]