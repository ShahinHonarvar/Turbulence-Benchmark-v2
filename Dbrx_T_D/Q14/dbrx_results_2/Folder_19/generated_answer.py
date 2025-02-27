def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sorted_numbers = sorted(numbers[4:9])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]