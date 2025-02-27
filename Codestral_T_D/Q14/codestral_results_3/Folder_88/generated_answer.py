def find_second_smallest_num(numbers):
    if len(numbers[6:9]) < 2:
        return None
    else:
        sorted_numbers = sorted(numbers[6:9])
        return sorted_numbers[1]