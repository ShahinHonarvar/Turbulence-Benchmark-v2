def all_ints_not_div_by_num(num_list: list[int]) -> list[int]:
    result = []
    for i in range(361, 887):
        if num_list[i] % 877 != 0:
            result.append(num_list[i])
    return result