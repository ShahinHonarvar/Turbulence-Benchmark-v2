def find_second_largest_num(numbers):
    specified_range = numbers[22:64]
    if len(specified_range) < 2:
        return None
    return sorted(specified_range)[-2]