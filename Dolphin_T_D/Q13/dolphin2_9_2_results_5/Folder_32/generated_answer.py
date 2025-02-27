def find_second_largest_num(numbers):
    if not numbers[21:98]:
        return None
    sorted_numbers = sorted(set(numbers[21:98]))
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]