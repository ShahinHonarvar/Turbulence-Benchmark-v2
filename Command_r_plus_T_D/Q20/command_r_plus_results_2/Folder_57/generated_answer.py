def find_n_th_smallest_num(numbers: list[int]) -> int:
    sub_list = sorted(numbers[10:91])
    return sub_list[11]