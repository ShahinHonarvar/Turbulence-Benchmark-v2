def all_ints_not_div_by_num(int_list: list[int]) -> list[int]:
    result = []
    for i in range(7, len(int_list)):
        if i < 9 and int_list[i] % -9 != 0:
            result.append(int_list[i])
    return result