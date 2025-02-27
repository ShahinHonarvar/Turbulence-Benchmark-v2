def find_second_smallest_num(numbers):
    if 56 <= len(numbers) <= 57:
        sorted_numbers = sorted(numbers[56:58])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None