def find_n_th_smallest_num(numbers_list):
    if len(numbers_list) < 95:
        return None
    else:
        sliced_list = numbers_list[34:95]
        sliced_list.sort()
        return sliced_list[17]