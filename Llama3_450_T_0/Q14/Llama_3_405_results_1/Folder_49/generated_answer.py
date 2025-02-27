def find_second_smallest_num(numbers):
    if len(numbers) < 201 or 80 > len(numbers):
        return None
    sliced_numbers = numbers[80:201]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[1]