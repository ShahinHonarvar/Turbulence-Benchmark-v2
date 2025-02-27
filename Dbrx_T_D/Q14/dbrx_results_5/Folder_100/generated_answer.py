def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sorted_numbers = sorted(set(numbers[43:52]))
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]