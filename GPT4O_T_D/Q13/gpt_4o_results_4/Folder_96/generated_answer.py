def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 16:
        return None
    sliced_numbers = numbers[15:52]
    unique_numbers = list(set(sliced_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]