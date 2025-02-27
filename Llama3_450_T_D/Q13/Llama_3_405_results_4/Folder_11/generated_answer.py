def find_second_largest_num(numbers):
    specified_range = numbers[37:52]
    if len(specified_range) < 2:
        return None
    specified_range.sort()
    return specified_range[-2]