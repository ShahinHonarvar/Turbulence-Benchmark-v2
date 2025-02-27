def find_second_smallest_num(numbers):
    specified_range = numbers[37:77]
    if len(specified_range) < 2:
        return None
    return sorted(specified_range)[1]