def find_second_smallest_num(numbers):
    if 30 <= len(numbers) <= 48:
        sorted_numbers = sorted(numbers[30:49])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None