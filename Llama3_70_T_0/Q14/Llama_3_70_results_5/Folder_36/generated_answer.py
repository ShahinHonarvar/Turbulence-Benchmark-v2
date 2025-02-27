def find_second_smallest_num(numbers):
    if len(numbers[209:557]) < 2:
        return None
    else:
        return sorted(numbers[209:557])[1]