def find_second_smallest_num(numbers):
    specific_range = numbers[68:87]
    if len(specific_range) < 2:
        return None
    return sorted(specific_range)[1]