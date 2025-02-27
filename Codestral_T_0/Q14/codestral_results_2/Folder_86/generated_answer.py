def find_second_smallest_num(numbers):
    if 33 <= len(numbers) <= 36:
        sorted_numbers = sorted(numbers[33:37])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None