def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    sliced_numbers = numbers[15:40]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[1]