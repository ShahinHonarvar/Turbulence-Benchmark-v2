def find_second_smallest_num(numbers):
    sliced_numbers = numbers[40:81]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]