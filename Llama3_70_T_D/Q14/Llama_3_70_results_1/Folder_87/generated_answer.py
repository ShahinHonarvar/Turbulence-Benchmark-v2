def find_second_smallest_num(numbers):
    sliced_numbers = numbers[22:89]
    if len(sliced_numbers) < 2:
        return None
    else:
        return sorted(sliced_numbers)[1]