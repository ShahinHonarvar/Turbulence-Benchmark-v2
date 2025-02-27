def find_second_smallest_num(lst):
    if not all((isinstance(i, (int, float)) for i in lst)):
        return 'Invalid input'
    if 40 <= len(lst) <= 80:
        new_lst = lst[39:81]
    elif len(lst) > 80:
        new_lst = lst[39:81]
    else:
        return 'None'
    if len(set(new_lst)) < 2:
        return 'None'
    new_lst.sort()
    return new_lst[1]