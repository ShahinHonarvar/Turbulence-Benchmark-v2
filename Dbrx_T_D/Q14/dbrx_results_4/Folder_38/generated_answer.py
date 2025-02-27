def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 51 or 37 > len(numbers) - 1:
        return None
    sorted_numbers = sorted(numbers[37:52])
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]