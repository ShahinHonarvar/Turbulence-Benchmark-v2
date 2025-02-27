def find_second_largest_num(numbers):
    if len(numbers) < 65:
        return None
    specified_range = numbers[14:65]
    if len(set(specified_range)) < 2:
        return None
    return sorted(set(specified_range))[-2]