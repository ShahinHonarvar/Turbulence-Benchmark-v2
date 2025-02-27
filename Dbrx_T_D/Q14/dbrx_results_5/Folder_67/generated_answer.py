def find_second_smallest_num(numbers):
    if len(numbers) < 55:
        return None
    sorted_numbers = sorted(numbers[50:55])
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]