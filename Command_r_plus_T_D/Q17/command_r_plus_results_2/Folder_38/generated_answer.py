def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    result = []
    for i in range(10, 77):
        if int_list[i] % -40 == 0 and int_list[i] % -12 == 0:
            result.append(int_list[i])
    return result