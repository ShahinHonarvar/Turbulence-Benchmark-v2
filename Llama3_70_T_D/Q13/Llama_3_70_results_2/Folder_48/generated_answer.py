def find_second_largest_num(numbers):
    if len(numbers[533:606]) < 2:
        return None
    else:
        return sorted(numbers[533:606], reverse=True)[1]