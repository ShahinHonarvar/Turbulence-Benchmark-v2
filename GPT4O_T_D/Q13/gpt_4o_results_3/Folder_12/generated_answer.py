def find_second_largest_num(numbers):
    if len(numbers) < 65:
        return None
    sub_list = numbers[14:65]
    if len(sub_list) < 2:
        return None
    sorted_sublist = sorted(sub_list, reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None