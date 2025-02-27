def find_second_smallest_num(numbers):
    sliced_numbers = numbers[90:201]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[1]