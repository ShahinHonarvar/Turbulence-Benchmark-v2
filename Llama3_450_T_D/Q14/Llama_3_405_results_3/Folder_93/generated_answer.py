def find_second_smallest_num(numbers):
    specified_range = numbers[75:89]
    if len(specified_range) < 2:
        return None
    else:
        return sorted(specified_range)[1]