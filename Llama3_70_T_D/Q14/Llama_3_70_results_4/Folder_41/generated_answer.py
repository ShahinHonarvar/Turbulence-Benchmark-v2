def find_second_smallest_num(numbers):
    return sorted(numbers[4:5])[1] if len(numbers[4:5]) > 1 else None