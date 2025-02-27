def find_second_largest_num(numbers):
    if len(numbers) < 83:
        return None
    sliced_numbers = sorted(numbers[56:83], reverse=True)
    if len(set(sliced_numbers)) < 2:
        return None
    return sliced_numbers[1]