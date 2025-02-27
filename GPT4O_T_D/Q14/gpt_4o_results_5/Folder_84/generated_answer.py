def find_second_smallest_num(numbers):
    sublist = numbers[40:81]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None