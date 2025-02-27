def find_second_smallest_num(numbers):
    sliced_numbers = numbers[26:53]
    if len(sliced_numbers) < 2:
        return None
    else:
        return sorted(sliced_numbers)[1]