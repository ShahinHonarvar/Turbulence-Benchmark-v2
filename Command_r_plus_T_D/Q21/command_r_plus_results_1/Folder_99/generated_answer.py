def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    result = []
    for i in range(161, 971):
        if int_list[i] % 763 == 0:
            result.append(int_list[i])
    return result