def all_ints_not_div_by_num(int_list: list[int]) -> list[int]:
    result = []
    for i in range(495, 826):
        if int_list[i] % -201 != 0:
            result.append(int_list[i])
    return result