def find_second_smallest_num(numbers):
    if len(numbers) < 606:
        return None
    sub_list = numbers[533:606]
    if len(set(sub_list)) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]