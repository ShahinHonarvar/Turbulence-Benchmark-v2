def find_second_smallest_num(numbers):
    if len(numbers[31:35]) < 2:
        return None
    return sorted(numbers[31:35])[1]