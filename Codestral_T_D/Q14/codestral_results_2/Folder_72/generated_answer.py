def find_second_smallest_num(numbers):
    if 82 <= len(numbers) <= 86:
        return None
    else:
        sorted_numbers = sorted(numbers[82:87])
        return sorted_numbers[1]