def find_second_smallest_num(numbers):
    if 42 <= len(numbers) <= 68:
        sorted_numbers = sorted(numbers[42:69])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None