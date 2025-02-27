def find_second_smallest_num(numbers):
    specified_range = numbers[310:371]
    if len(specified_range) < 2:
        return None
    specified_range.sort()
    return specified_range[1]