def find_second_smallest_num(numbers):
    if 75 <= len(numbers) <= 88:
        sorted_numbers = sorted(numbers[75:89])
        if len(sorted_numbers) >= 2:
            return sorted_numbers[1]
    return None