def find_second_largest_num(lst):
    if len(lst) <= 40 or len(lst) < 201:
        return None
    sub_lst = lst[40:201]
    unique_numbers = list(set(sub_lst))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]