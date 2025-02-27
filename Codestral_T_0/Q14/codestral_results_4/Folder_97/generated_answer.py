def find_second_smallest_num(numbers):
    if 31 <= len(numbers) <= 34:
        sorted_numbers = sorted(numbers[31:35])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None