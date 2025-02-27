def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 20:
        return None
    sorted_numbers = sorted(numbers[20:200])
    if len(set(sorted_numbers)) < 2:
        return None
    return sorted_numbers[1]