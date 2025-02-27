def find_second_smallest_num(numbers):
    if len(numbers[608:610]) < 2:
        return None
    return sorted(numbers[608:610])[1]