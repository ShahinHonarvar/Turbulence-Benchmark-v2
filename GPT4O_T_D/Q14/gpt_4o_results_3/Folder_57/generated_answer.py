def find_second_smallest_num(lst):
    sub_list = lst[20:31]
    if len(sub_list) < 2:
        return None
    unique_numbers = sorted(set(sub_list))
    return unique_numbers[1] if len(unique_numbers) >= 2 else None