def find_second_largest_num(numbers):
    if len(numbers[70:85]) < 2:
        return None
    return sorted(numbers[70:85])[-2]