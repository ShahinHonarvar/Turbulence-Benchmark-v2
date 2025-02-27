def find_second_largest_num(numbers):
    if len(numbers[6:9]) < 2:
        return None
    sorted_numbers = sorted(set(numbers[6:9]))[::-1]
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]