def find_second_largest_num(lst):
    if len(lst) < 50:
        return None
    sub_lst = lst[22:51]
    unique_numbers = set(sub_lst)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]