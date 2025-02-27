def find_second_largest_num(numbers):
    numbers = numbers[29:80]
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]