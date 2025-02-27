def find_second_largest_num(numbers):
    numbers_in_range = numbers[0:4]
    unique_numbers = list(set(numbers_in_range))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    else:
        return unique_numbers[1]