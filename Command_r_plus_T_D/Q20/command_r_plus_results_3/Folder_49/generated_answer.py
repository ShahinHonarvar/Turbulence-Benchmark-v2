def find_n_th_smallest_num(numbers_list: list[int]) -> int:
    sliced_list = sorted(numbers_list[20:201])
    return sliced_list[10]