def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 8:
        return None
    sorted_numbers = sorted(numbers[:8])
    if sorted_numbers[1] == sorted_numbers[0]:
        return None
    else:
        return sorted_numbers[1]