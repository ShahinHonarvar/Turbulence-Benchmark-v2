def find_second_smallest_num(numbers):
    if 310 <= len(numbers) <= 370:
        sliced_numbers = numbers[310:371]
        sorted_numbers = sorted(sliced_numbers)
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None