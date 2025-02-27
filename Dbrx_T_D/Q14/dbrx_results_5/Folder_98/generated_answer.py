def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sorted_numbers = sorted(numbers[6:7])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]