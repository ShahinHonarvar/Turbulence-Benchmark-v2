def find_second_smallest_num(numbers):
    if len(numbers[70:85]) < 2:
        return None
    else:
        return sorted(numbers[70:85])[1]