def find_second_smallest_num(numbers):
    if 34 <= len(numbers) <= 55:
        sorted_numbers = sorted(numbers[34:56])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None