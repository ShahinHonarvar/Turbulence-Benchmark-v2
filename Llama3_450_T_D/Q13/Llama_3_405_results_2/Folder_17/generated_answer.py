def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    specified_range = numbers[62:79]
    if len(specified_range) < 2:
        return None
    return sorted(specified_range)[-2]