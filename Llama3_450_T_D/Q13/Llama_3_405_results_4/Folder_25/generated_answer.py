def find_second_largest_num(numbers):
    specified_range = numbers[29:94]
    if len(specified_range) < 2:
        return None
    else:
        return sorted(specified_range)[-2]