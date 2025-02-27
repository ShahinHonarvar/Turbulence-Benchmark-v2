def find_second_largest_num(numbers):
    if len(numbers) < 976:
        return None
    sub_list = numbers[639:976]
    if len(sub_list) < 2:
        return None
    sub_list_sorted = sorted(sub_list, reverse=True)
    return sub_list_sorted[1] if len(sub_list_sorted) > 1 else None