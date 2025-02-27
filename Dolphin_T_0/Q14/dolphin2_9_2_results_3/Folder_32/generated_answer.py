def find_second_smallest_num(numbers):
    if len(numbers[32:36]) < 2:
        return None
    else:
        return sorted(numbers[32:36])[1]