def find_second_smallest_num(numbers):
    if len(numbers[34:56]) <= 1:
        return None
    elif len(numbers[34:56]) == 2:
        return min(numbers[34:56])
    else:
        sorted_numbers = sorted(numbers[34:56])
        return sorted_numbers[1]