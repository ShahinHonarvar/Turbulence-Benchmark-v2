def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 8:
        return None
    sorted_numbers = sorted(set(numbers[:8]))
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]