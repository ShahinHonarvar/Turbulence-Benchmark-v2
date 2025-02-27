def find_second_smallest_num(numbers):
    if 5 <= len(numbers) <= 7:
        sorted_numbers = sorted(numbers[5:8])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None