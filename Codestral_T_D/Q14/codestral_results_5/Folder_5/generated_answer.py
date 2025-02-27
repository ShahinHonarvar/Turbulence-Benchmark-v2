def find_second_smallest_num(numbers):
    if len(numbers[3:6]) < 2:
        return None
    else:
        sorted_numbers = sorted(numbers[3:6])
        return sorted_numbers[1]