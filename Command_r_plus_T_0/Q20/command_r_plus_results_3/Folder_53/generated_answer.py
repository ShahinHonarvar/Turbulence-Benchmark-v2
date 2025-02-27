def find_n_th_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 191:
        return None
    return sorted(numbers_list[18:191])[18]