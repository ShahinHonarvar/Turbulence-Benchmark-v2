def find_second_smallest_num(num_list):
    if len(num_list[246:751]) < 2:
        return None
    else:
        return sorted(set(num_list[246:751]))[1]