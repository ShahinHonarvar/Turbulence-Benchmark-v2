def find_second_largest_num(numbers):
    if len(numbers) < 77:
        return None
    specified_range = numbers[37:77]
    sorted_range = sorted(specified_range, reverse=True)
    if len(sorted_range) < 2:
        return None
    return sorted_range[1]