def find_second_smallest_num(numbers):
    specified_range = numbers[10:67]
    if len(specified_range) < 2:
        return None
    else:
        specified_range.sort()
        return specified_range[1]