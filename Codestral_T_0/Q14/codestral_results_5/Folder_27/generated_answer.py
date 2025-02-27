def find_second_smallest_num(numbers):
    if 25 <= len(numbers) <= 59:
        sorted_numbers = sorted(numbers[25:60])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None