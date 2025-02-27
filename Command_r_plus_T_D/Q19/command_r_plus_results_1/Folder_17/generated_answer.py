def all_ints_not_div_by_num(num_list: list[int]) -> list[int]:
    result = []
    for i in range(39, 57):
        if num_list[i] % 84 != 0:
            result.append(num_list[i])
    return result