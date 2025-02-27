def find_second_smallest_num(numbers):
    if len(numbers) < 2 or not all((isinstance(i, (int, float)) for i in numbers)):
        return None
    unique_numbers = set(numbers)
    sorted_numbers = sorted(unique_numbers)[74:96]
    if len(sorted_numbers) < 2:
        return None
    return sorted(sorted_numbers)[1]