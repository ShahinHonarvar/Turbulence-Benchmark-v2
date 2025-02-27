def find_second_largest_num(num_list):
    try:
        num_list_sorted = sorted(num_list[310:371])
        return num_list_sorted[-2]
    except IndexError:
        return None