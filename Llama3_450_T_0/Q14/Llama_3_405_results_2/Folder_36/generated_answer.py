def find_second_smallest_num(numbers):
    if len(numbers) < 557 or 209 > len(numbers):
        return None
    sliced_numbers = numbers[209:557]
    sorted_numbers = sorted(sliced_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]