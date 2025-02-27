def find_second_largest_num(numbers):
    sliced_numbers = sorted(numbers[55:99], reverse=True)
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]