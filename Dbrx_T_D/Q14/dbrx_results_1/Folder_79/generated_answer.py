def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    sorted_numbers = sorted(list(set(numbers[1:6])))
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]