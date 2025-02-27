def find_second_smallest_num(numbers):
    if len(numbers[1:6]) < 2:
        return None
    else:
        sorted_numbers = sorted(numbers[1:6])
        return sorted_numbers[1]