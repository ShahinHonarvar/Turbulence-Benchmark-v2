def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) <= 70:
        return None
    sliced_numbers = numbers[70:201]
    sorted_numbers = sorted(sliced_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]