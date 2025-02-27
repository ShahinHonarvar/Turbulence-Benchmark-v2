def all_ints_not_div_by_num(int_list: list[int]) -> list[int]:
    result = []
    for i in range(50, 92):
        if int_list[i] % 16 != 0:
            result.append(int_list[i])
    return result