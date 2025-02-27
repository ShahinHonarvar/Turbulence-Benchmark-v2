def find_second_smallest_num(num_list):
    try:
        num_list[66:94].sort()
        return num_list[66]
    except IndexError:
        return None