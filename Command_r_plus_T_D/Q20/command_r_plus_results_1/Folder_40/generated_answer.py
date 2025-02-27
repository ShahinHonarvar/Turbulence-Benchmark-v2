def find_n_th_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 5:
        return None
    return sorted(numbers_list)[:5][-1]