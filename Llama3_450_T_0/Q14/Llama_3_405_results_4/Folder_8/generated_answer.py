def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    sliced_numbers = numbers[56:67]
    sorted_numbers = sorted(sliced_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]