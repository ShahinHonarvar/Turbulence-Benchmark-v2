def find_second_largest_num(numbers):
    if len(numbers) < 606:
        return None
    sub_list = numbers[533:606]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[-2]