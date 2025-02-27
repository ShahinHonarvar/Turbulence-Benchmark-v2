def find_second_smallest_num(lst):
    if 40 <= len(lst) <= 80:
        try:
            return sorted(lst[40:81])[1]
        except IndexError:
            return 'None'
    else:
        return 'None'