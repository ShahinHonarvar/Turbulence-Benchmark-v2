def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    sorted_numbers = sorted(numbers[8:10])
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]