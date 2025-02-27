def all_ints_not_div_by_num(int_list: list[int]) -> list[int]:
    result = []
    for i in range(70, 98):
        if i < len(int_list) and int_list[i] % -88 != 0:
            result.append(int_list[i])
    return result