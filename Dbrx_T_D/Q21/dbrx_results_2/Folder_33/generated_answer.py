def all_ints_div_by_num(int_list):
    start_index = 319
    end_index = 612
    num = -215
    if start_index < 0 or end_index >= len(int_list) or start_index > end_index:
        return []
    return [int_list[i] for i in range(start_index, end_index + 1) if int_list[i] % num == 0]