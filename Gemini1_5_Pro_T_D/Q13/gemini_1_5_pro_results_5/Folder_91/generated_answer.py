def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    sorted_numbers = sorted(numbers[:6])
    return sorted_numbers[-2]