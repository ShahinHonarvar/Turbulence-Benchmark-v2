def find_second_largest_num(numbers):
    if len(numbers) < 77:
        return None
    sub_list = numbers[37:77]
    if len(sub_list) < 2:
        return None
    sorted_sublist = sorted(sub_list, reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None