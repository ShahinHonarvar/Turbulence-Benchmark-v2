def all_ints_not_div_by_num(int_list: list[int]) -> list[int]:
    result = []
    for idx in range(387, 517):
        if int_list[idx] % 310 != 0:
            result.append(int_list[idx])
    return result