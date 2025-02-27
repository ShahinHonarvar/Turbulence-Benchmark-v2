def find_second_largest_num(numbers):
    specified_range = numbers[29:94]
    if len(specified_range) < 2:
        return None
    specified_range.sort(reverse=True)
    return specified_range[1]