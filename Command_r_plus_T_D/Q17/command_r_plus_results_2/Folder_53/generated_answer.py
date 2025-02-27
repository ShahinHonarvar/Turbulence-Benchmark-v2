def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    result = []
    for i in range(200, len(int_list)):
        if int_list[i] % 17 == 0 and int_list[i] % -5 == 0:
            result.append(int_list[i])
    return result