def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sorted_numbers = sorted(numbers[5:8])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]