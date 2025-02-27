def find_n_th_smallest_num(numbers_list: list[int]) -> int:
    sliced_list = numbers_list[43:81]
    sliced_list.sort()
    return sliced_list[5]