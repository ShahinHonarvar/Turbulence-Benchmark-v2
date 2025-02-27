def find_second_largest_num(numbers):
    if 93 < len(numbers) < 66:
        return None
    sub_numbers = numbers[66:94]
    if len(sub_numbers) < 2:
        return None
    max_num = max(sub_numbers)
    sub_numbers.remove(max_num)
    if len(sub_numbers) < 1:
        return None
    second_max_num = max(sub_numbers)
    return second_max_num