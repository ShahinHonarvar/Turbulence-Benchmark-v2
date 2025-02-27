def find_second_largest_num(numbers):
    sliced_numbers = numbers[28:41]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]