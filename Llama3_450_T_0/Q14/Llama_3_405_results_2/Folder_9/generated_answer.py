def find_second_smallest_num(numbers):
    if len(numbers) < 201 or 70 > len(numbers):
        return None
    sliced_numbers = numbers[70:201]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[1]