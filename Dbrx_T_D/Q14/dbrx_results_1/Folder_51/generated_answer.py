def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 9:
        return None
    sorted_numbers = sorted(numbers[1:9])
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]