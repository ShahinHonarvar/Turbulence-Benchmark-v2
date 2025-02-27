def find_second_largest_num(numbers):
    unique_numbers = list(set(numbers[1:6]))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]