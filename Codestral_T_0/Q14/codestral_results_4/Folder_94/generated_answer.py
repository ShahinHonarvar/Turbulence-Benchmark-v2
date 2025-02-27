def find_second_smallest_num(numbers):
    if 52 <= len(numbers) <= 71:
        sorted_numbers = sorted(numbers[52:72])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None