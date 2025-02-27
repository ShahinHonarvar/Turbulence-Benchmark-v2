def find_second_smallest_num(numbers):
    if len(numbers) < 55:
        return None
    numbers_slice = numbers[50:55]
    sorted_numbers_slice = sorted(numbers_slice)
    if len(sorted_numbers_slice) < 2:
        return None
    return sorted_numbers_slice[1]