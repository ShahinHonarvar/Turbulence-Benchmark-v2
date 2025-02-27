def find_second_largest_num(numbers):
    sliced_numbers = numbers[686:988]
    if len(sliced_numbers) < 2:
        return None
    else:
        return sorted(sliced_numbers)[-2]