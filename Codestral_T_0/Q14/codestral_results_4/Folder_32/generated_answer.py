def find_second_smallest_num(numbers):
    if 32 <= len(numbers) <= 35:
        sorted_numbers = sorted(numbers[32:36])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None