def find_second_smallest_num(numbers):
    if len(numbers[12:93]) < 2:
        return None
    else:
        sorted_numbers = sorted(numbers[12:93])
        return sorted_numbers[1]