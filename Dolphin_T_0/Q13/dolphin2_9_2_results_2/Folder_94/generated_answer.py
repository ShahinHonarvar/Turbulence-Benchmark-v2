def find_second_largest_num(numbers):
    sliced_numbers = numbers[28:41]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers, reverse=True)
    if sorted_numbers[0] == sorted_numbers[1]:
        return None
    return sorted_numbers[1]