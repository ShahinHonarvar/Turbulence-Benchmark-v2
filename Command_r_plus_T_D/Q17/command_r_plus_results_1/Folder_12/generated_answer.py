def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    result = []
    for i in range(35, 65):
        if int_list[i] % -30 == 0 and int_list[i] % -95 == 0:
            result.append(int_list[i])
    return result