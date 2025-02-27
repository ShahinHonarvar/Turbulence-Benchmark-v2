def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 556 >= len(numbers) or 209 < 0:
        return None
    sliced_numbers = numbers[209:557]
    sorted_numbers = sorted(sliced_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]