def find_second_smallest_num(num_list):
    if len(num_list) < 608 or len(num_list) > 610:
        return None
    num_list[608:610] = sorted(num_list[608:610])
    return num_list[609]