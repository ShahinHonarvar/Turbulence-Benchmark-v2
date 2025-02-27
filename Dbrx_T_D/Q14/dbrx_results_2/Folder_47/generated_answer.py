def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 53:
        return None
    sorted_numbers = sorted(numbers[22:64])
    if len(set(sorted_numbers)) < 2:
        return None
    return sorted_numbers[1]