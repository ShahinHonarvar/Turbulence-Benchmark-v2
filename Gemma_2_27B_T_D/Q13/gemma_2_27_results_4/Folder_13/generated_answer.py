def find_second_largest_num(numbers):
    if len(numbers[25:88]) < 2:
        return None
    return sorted(numbers[25:88])[-2]