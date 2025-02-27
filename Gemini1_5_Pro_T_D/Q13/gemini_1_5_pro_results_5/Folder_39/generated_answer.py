def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    sliced_numbers = numbers[20:31]
    if len(set(sliced_numbers)) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[-2]