def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    numbers = numbers[5:8]
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]