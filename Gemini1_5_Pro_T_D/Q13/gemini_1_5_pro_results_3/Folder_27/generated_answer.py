def find_second_largest_num(numbers):
    if len(numbers) < 94 or len(numbers) < 66:
        return None
    sliced_numbers = numbers[66:94]
    if len(set(sliced_numbers)) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[-2]