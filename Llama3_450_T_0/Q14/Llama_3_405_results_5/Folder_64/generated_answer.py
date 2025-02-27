def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 5:
        return None
    sorted_numbers = sorted(numbers[:5])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]